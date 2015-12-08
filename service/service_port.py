# -*- coding: utf-8 -*-
import web
import db
import sys
import json
import psutil
import platform

render = web.template.render('templates/')

def CmpPid(a, b):
    if a['Pid'] < b['Pid']:
        return -1
    elif a['Pid'] > b['Pid']:
        return 1
    else:
        return 0
        
class port_list_query:
    
    
    def GET(self):
        PortList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 0,
        }
        
        param = web.input()
        if param.has_key('Length') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Length=Length'
            return render.port_list(json.dumps(PortList))
        if param.has_key('Start') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Start=Start'
            return render.port_list(json.dumps(PortList))
        
        start  = int(param['Start'])
        length = int(param['Length'])

        # 获取所有连接
        Lists = []
        cons = psutil.net_connections('inet')
        for c in cons:
            dic = {}
            if c.type == 1:
                dic['Type'] = 'TCP'
            elif c.type == 2:
                dic['Type'] = 'UDP'
            # sip sport 
            if len(c.laddr) > 0:
                dic['Sip']   = c.laddr[0]
                dic['Sport'] = str(c.laddr[1])
            else:
                dic['Sip']   = 'NULL'
                dic['Sport'] = '0'
            # dip dport
            if len(c.raddr) > 0:
                dic['Dip']   = c.raddr[0]
                dic['Dport'] = str(c.raddr[1])
            else:
                dic['Dip']   = 'NULL'
                dic['Dport'] = '0'
            dic['Status'] = c.status
            dic['Pid'] = str(c.pid)

            #print c.raddr
            p = psutil.Process(c.pid)
            # name
            dic['Process'] = p.exe()
            # 加入数组
            Lists.append(dic)

        # 排序
        Lists.sort(CmpPid)
        PortList['Lists'] = Lists[start : start + length]
        PortList['Totle'] = len(Lists)
        return render.port_list(json.dumps(PortList))
    
    def POST(self):
        return self.GET()

