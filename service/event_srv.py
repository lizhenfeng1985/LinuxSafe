# -*- coding: utf-8 -*-

import socket
import select 
import struct
import threading
import event_url
Tst_Sendstr = "welcome epoll server"

SERVER_HOST  = 'localhost'
KERNMSG_RECV_LEN = 872
KERNMSG_SEND_LEN = 4


def FilterMsg(msg):
	allow  = struct.pack("I", 0)
	forbid = struct.pack("I", 1)
	ret = [0, allow]
	try:
		op_type, uid, sub_pid, obj_pid, sub_proc, host, uri, sip_dip = struct.unpack("4I264s264s264s64s", msg)
		sub_proc= sub_proc.split('\x00')[0]
		sip_dip = sip_dip.split('\x00')[0]
		host    = host.split('\x00')[0]
		uri     = uri.split('\x00')[0]

		if op_type == 63 : # url
                        print '[URL][%d][%s][%s][%s]' % (op_type, sub_proc, sip_dip, host + uri)
                        r = event_url.UrlCheck(host, uri)
                        if r == 1 : # 禁止访问
                                ret = [0, forbid]
                        print ret
                else:
                        print '[%d][%s]' % (op_type, sub_proc)
	except:
		print "ERR unpack len = ", len(msg)
	return ret

class EpollServer(object):
	'''A socket server using Epoll'''

	def __init__(self, host=SERVER_HOST, port=7000):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((host, port))
		self.sock.listen(1)
		self.sock.setblocking(0)
		self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		print 'Started Epoll Server on [%s:%d]' % (host, port)
		self.epoll = select.epoll()
		self.epoll.register(self.sock.fileno(), select.EPOLLIN)

	def run(self):
		'''Executes epoll server operation'''

		try:
			connections = {}
			requests    = {}
			responses   = {}
			while True:
				events = self.epoll.poll(1)
				for fileno, event in events:
					# new connect 
					if fileno == self.sock.fileno():
						connection, address = self.sock.accept()
						connection.setblocking(0)
						self.epoll.register(connection.fileno(), select.EPOLLIN)
						connections[connection.fileno()] = connection
						responses[connection.fileno()] = ''
						requests[connection.fileno()] = ''
						print 'connect :', address
					elif event & select.EPOLLIN:
						data = connections[fileno].recv(KERNMSG_RECV_LEN)
						if not data:
							self.epoll.modify(fileno, 0)
							print "close   :", connections[fileno].getpeername()
							connections[fileno].shutdown(socket.SHUT_RDWR)

						#print 'client data :', data
						requests[fileno] += data
						if len(requests[fileno]) >= KERNMSG_RECV_LEN:
							# 消息处理
							ret = FilterMsg(requests[fileno])
							responses[fileno] += ret[1][:KERNMSG_SEND_LEN]
							self.epoll.modify(fileno, select.EPOLLOUT)
					elif event & select.EPOLLOUT:
						reslen = len(responses[fileno])
						if reslen < KERNMSG_SEND_LEN:
							self.epoll.modify(fileno, select.EPOLLIN)
						#elif reslen == 0:
						#	self.epoll.modify(fileno, 0)
						#	print "close   :", connections[fileno].getpeername()
						#	connections[fileno].shutdown(socket.SHUT_RDWR)
						else:
							byteswritten = connections[fileno].send(responses[fileno][:KERNMSG_SEND_LEN])
							if byteswritten <= 0:
								self.epoll.modify(fileno, select.EPOLLIN)
							else:
								# 去掉request中已经处理掉的消息
								requests[fileno] = requests[fileno][KERNMSG_RECV_LEN:]
								#print 'send data(%s) : %s' % (byteswritten, responses[fileno][:byteswritten])
								responses[fileno] = responses[fileno][byteswritten:]
					elif event & select.EPOLLHUP:
						self.epoll.unregister(fileno)
						connections[fileno].close()
						del connections[fileno]
		finally:
			self.epoll.unregister(self.sock.fileno())
			self.epoll.close()
			self.sock.close()


if __name__ == '__main__':
	server = EpollServer()
	server.run()

