# -*- coding: utf-8 -*-

import config
import sqlite3
import os
import threading

# 全局变量
global GLOGCONN    # sqlite连接
global GLOGCUR     # sqlite游标
global GLOGLSTS    # 日志记录
global GLOGDEBUG   # 调试模式
global GLOGMUTEX   # 线程锁
global GLOGEXIT    # 退出标志
GLOGMUTEX = threading.Lock() 
GLOGCONN  = None
GLOGCUR   = None
GLOGLSTS  = []
GLOGEXIT  = False
GLOGDEBUG = True


def Connect():
    global GLOGCONN
    global GLOGCUR
    needCreateTb = False
    cfg = config.ReadConfig()
    try:
        dbname = cfg.get("LogDb", "LogDbName")
    except Exception as e:
        print ("[Error] config.get(DataBase, DbName)")
        print (e.message)
        return -1

    if os.path.exists(dbname) == False:
        needCreateTb = True
    
    try:
        con = sqlite3.connect(dbname, check_same_thread = False)
    except Exception as e:
        print ("[Error] sqlite3.connect(%s)" % (dbname))
        print (e.message)
        return -1
    
    GLOGCONN = con
    GLOGCUR = con.cursor()

    if needCreateTb:
        ret = CreateTb_Log()
        return ret[0]
    return 0

    
def Close():
    global GLOGCONN
    global GLOGCUR
    GLOGCUR.close()
    GLOGCONN.close()


# 执行一条语句
def SqlExecute(sql):
    global GLOGCONN
    global GLOGCUR
    global GLOGDEBUG
    if GLOGDEBUG:
        print ("[Debug] SqlExecute : %s" % (sql))
    try:
        GLOGCUR.execute(sql)
        GLOGCONN.commit()
    except Exception as e:
        print ("[Error] SqlExecute : %s" % (sql))
        print (e.message)
        return (-1, "Failed:" + e.message)
    return (0, "OK")


# 执行一条查询语句并获取结果
def SqlQuery(sql):
    global GLOGCONN
    global GLOGCUR
    global GLOGDEBUG
    if GLOGDEBUG:
        print ("[Debug] SqlQuery : %s" % (sql))
    try:
        GLOGCUR.execute(sql)
        GLOGCONN.commit()
    except Exception as e:
        print ("[Error] SqlQuery : %s" % (sql))
        print (e.message)
        return [-1, "Failed:" + e.message, None]
    
    r = GLOGCUR.fetchall()
    return [0, "OK", r]



# Url查询
def LogUrlQuery(start, length, startTime, stopTime, keyWord):
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Lists'   : [],
         'Totle'   : 0,
    }

    # 获取总数量
    sql = u'select count(*) from log where type like "URL-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" or ' % (keyWord) + \
          u' objdstpath like "%%%s%%" or ' % (keyWord) + \
          u' sipdip like "%%%s%%" or ' % (keyWord) + \
          u' perm like "%%%s%%" ) ' % (keyWord)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList
    retList['Totle'] = ret[2][0][0]
    
    # 查询当前条件数据
    sql = u'select type, subpid, user, subproc, sipdip, objsrcpath, objdstpath, perm, time from log where type like "URL-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" or ' % (keyWord) + \
          u' objdstpath like "%%%s%%" or ' % (keyWord) + \
          u' sipdip like "%%%s%%" or ' % (keyWord) + \
          u' perm like "%%%s%%" ) ' % (keyWord) + \
          u' order by id desc limit %d, %d ' % (start, length)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    for u in ret[2]:
        lst = {
            'Type'    : u[0],
            'Pid'     : u[1],
            'User'    : u[2],
            'Subproc' : u[3],
            'Sipdip'  : u[4],
            'Host'    : u[5],
            'Uri'     : u[6],
            'Perm'    : u[7],
            'Time'    : u[8],
        }
        retList['Lists'].append(lst)
    return retList

# 查询特殊资源保护日志
def LogSpecrcQuery(start, length, startTime, stopTime, keyWord):
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Lists'   : [],
         'Totle'   : 0,
    }

    # 获取总数量
    sql = u'select count(*) from log where type like "特殊资源-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" or ' % (keyWord) + \
          u' perm like "%%%s%%" ) ' % (keyWord)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList
    retList['Totle'] = ret[2][0][0]
    
    # 查询当前条件数据
    sql = u'select subpid, user, subproc, objsrcpath, perm, time from log where type like "特殊资源-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" or ' % (keyWord) + \
          u' perm like "%%%s%%" ) ' % (keyWord) + \
          u'order by id desc limit %d, %d ' % (start, length)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    for u in ret[2]:
        lst = {
            'Pid'     : u[0],
            'User'    : u[1],
            'Subproc' : u[2],
            'ObjSrc'  : u[3],
            'Perm'    : u[4],
            'Time'    : u[5],
        }
        retList['Lists'].append(lst)
    return retList


# 查询外设保护日志
def LogDeviceQuery(start, length, startTime, stopTime, keyWord):
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Lists'   : [],
         'Totle'   : 0,
    }

    # 获取总数量
    sql = u'select count(*) from log where type like "外设管理-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" or ' % (keyWord) + \
          u' perm like "%%%s%%" ) ' % (keyWord)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList
    retList['Totle'] = ret[2][0][0]
    
    # 查询当前条件数据
    sql = u'select subpid, user, subproc, objsrcpath, perm, time from log where type like "外设管理-%%" and ' + \
          u'time >= "%s" and ' % (startTime) + \
          u'time <= "%s" and ' % (stopTime) + \
          u'( type like "%%%s%%" or ' % (keyWord) + \
          u' user like "%%%s%%" or ' % (keyWord) + \
          u' subpid like "%%%s%%" or ' % (keyWord) + \
          u' subproc like "%%%s%%" or ' % (keyWord) + \
          u' objsrcpath like "%%%s%%" ) ' % (keyWord) + \
          u' order by id desc limit %d, %d ' % (start, length)
    
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    for u in ret[2]:
        lst = {
            'Pid'     : u[0],
            'User'    : u[1],
            'Subproc' : u[2],
            'ObjSrc'  : u[3],
            'Perm'    : u[4],
            'Time'    : u[5],
        }
        retList['Lists'].append(lst)
    return retList


# 创建日志表
def CreateTb_Log():
    global GLOGCUR
    global GLOGDEBUG

    # 创建log表
    sql = '''create table if not exists log (
	id integer not null primary key,
	type        char(16) not null,
	user        char(64) not null,
	subpid      char(8) not null,
	objpid      char(8) not null,
	subproc     varchar(264) not null,
	objsrcpath  varchar(264) not null,
	objdstpath  varchar(264) not null,
	sipdip      varchar(64) not null,	
	status      char(12) not null,
	perm        char(12) not null,
	time        datetime
    );'''
    ret = SqlExecute(sql)
    if ret[0] != 0 :
        return ret
    return ret

# 添加一条记录到log队列中
def LogAddOne(sql):
    global GLOGMUTEX
    global GLOGLSTS
        
    if GLOGMUTEX.acquire(1):
            GLOGLSTS.append(sql)
            GLOGMUTEX.release()
    return 0

# 处理log消息
def LogRunThread():
    global GLOGMUTEX
    global GLOGLSTS
    global GLOGEXIT

    while 1:
        if GLOGEXIT == True:
            break
        if GLOGMUTEX.acquire(1):
                sqls = GLOGLSTS
                GLOGLSTS = []
                GLOGMUTEX.release()

        for sql in sqls:
            ret = SqlExecute(sql)
            if ret[0] != 0 :
                print ("[Error:] SqlExecute : %s" % (sql))

    #清理剩余数据
    if GLOGMUTEX.acquire(1):
        sqls = GLOGLSTS
        GLOGLSTS = []
        GLOGMUTEX.release()

    for sql in sqls:
        ret = SqlExecute(sql)
        if ret[0] != 0 :
            print ("[Error:] SqlExecute : %s" % (sql))
            
    # 关闭接口
    Close()
    return 0

if __name__ == "__main__":
    cn = Connect()
    if cn != None:
        print LogUrlQuery(2, 4, "2015-11-06 00:00:00", "2015-11-19 00:00:00", '')
        print LogSpecrcQuery(4, 6, "2015-11-06 00:00:00", "2015-11-19 00:00:00", '')
        print LogDeviceQuery(0, 2, "2015-11-06 00:00:00", "2015-11-19 00:00:00", '外设')
        
        Close()
