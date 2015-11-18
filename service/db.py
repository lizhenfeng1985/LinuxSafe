# -*- coding: utf-8 -*-


import config
import sqlite3
import os
import threading

# 全局变量
global GCONN    # sqlite连接
global GCUR     # sqlite游标
global GDEBUG   # 调试模式
GMUTEX = threading.Lock() # 线程锁
GCONN  = None
GCUR   = None
GDEBUG = False


def Connect():
    global GCONN
    global GCUR
    needCreateTb = False
    cfg = config.ReadConfig()
    try:
        dbname = cfg.get("DataBase", "DbName")
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
    
    GCONN = con
    GCUR = con.cursor()

    if needCreateTb:
        CreateTb_Url()
    return 0

    
def Close(con):
    global GCONN
    global GCUR
    GCUR.close()
    GCONN.close()


# 执行一条语句
def SqlExecute(sql):
    global GCONN
    global GCUR
    global GDEBUG
    if GDEBUG:
        print ("[Debug] SqlExecute : %s" % (sql))
    try:
        GCUR.execute(sql)
        GCONN.commit()
    except Exception as e:
        print ("[Error] SqlExecute : %s" % (sql))
        print (e.message)
        return (-1, "Failed:" + e.message)
    return (0, "OK")


# 执行一条查询语句并获取结果
def SqlQuery(sql):
    global GCONN
    global GCUR
    global GDEBUG
    if GDEBUG:
        print ("[Debug] SqlQuery : %s" % (sql))
    try:
        GCUR.execute(sql)
        GCONN.commit()
    except Exception as e:
        print ("[Error] SqlQuery : %s" % (sql))
        print (e.message)
        return [-1, "Failed:" + e.message, None]
    
    r = GCUR.fetchall()
    return [0, "OK", r]


# Url添加 t=0白名单 t=1黑名单
def UrlAdd(url, t):
    if t == 0:
        sql = sql = 'insert into url (id, url, type) values (null, "%s", 0)' % (url)
    else:
        sql = sql = 'insert into url (id, url, type) values (null, "%s", 1)' % (url)
        
    ret = SqlExecute(sql)
    return ret


# Url删除 t=0白名单 t=1黑名单
def UrlDel(url):
    sql = sql = 'delete from url where url = "%s"' % (url)
    ret = SqlExecute(sql)
    return ret


# Url查询 t=0白名单 t=1黑名单
def UrlQuery(t, start, length):
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Lists'   : [],
         'Totle'   : 0,
    }

    # 获取总数量
    if t == 0:
        sql = 'select count(*) from url where type == 0'
    else:
        sql = 'select count(*) from url where type == 1'
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList
    retList['Totle'] = ret[2][0][0]
    
    # 查询当前条件数据
    if t == 0:
        sql = 'select url from url where type == 0 order by id desc limit %d, %d' % (start, length)
    else:
        sql = 'select url from url where type == 1 order by id desc limit %d, %d' % (start, length)
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList
    for u in ret[2]:
        retList['Lists'].append(u[0])
    return retList


# Cnfig查询
def ConfigGet():
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Config'  : {},
    }
    
    # 查询
    sql = 'select url_white, url_black from config where id == 1'
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    if len(ret[2]) != 1:
        retList['ErrStat'] = -1
        retList['ErrMsg'] = u'Failed: 查询config失败'
        return retList

    retList['Config']['White_Start'] = ret[2][0][0]
    retList['Config']['Black_Start'] = ret[2][0][1]
    return retList

# Cnfig设置
def ConfigSet(url_white, url_black):
    # 更新
    sql = 'update config set url_white = %d, url_black = %d where id == 1' % (url_white, url_black)
    ret = SqlExecute(sql)
    return ret

# Cnfig查询Device
def ConfigGetDevice():
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Config'  : {},
    }
    
    # 查询
    sql = 'select device_cdrom, device_usb from config where id == 1'
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    if len(ret[2]) != 1:
        retList['ErrStat'] = -1
        retList['ErrMsg'] = u'Failed: 查询config_device失败'
        return retList

    retList['Config']['CdromStatus'] = ret[2][0][0]
    retList['Config']['UsbStatus']   = ret[2][0][1]
    return retList

# Cnfig设置Device
def ConfigSetDevice(device_cdrom, device_usb):
    # 更新
    sql = 'update config set device_cdrom = %d, device_usb = %d where id == 1' % (device_cdrom, device_usb)
    ret = SqlExecute(sql)
    return ret

# Cnfig查询Specrc特殊资源
def ConfigGetSpecrc():
    retList = {
         'ErrStat' : 0,
         'ErrMsg'  : 'OK',
         'Config'  : {},
    }
    
    # 查询
    sql = 'select specrc_shutdown, specrc_time from config where id == 1'
    ret = SqlQuery(sql)
    if ret[0] != 0:
        retList['ErrStat'] = ret[0]
        retList['ErrMsg'] = ret[1]
        return retList

    if len(ret[2]) != 1:
        retList['ErrStat'] = -1
        retList['ErrMsg'] = u'Failed: 查询config_specrc失败'
        return retList

    retList['Config']['ShutDownStatus'] = ret[2][0][0]
    retList['Config']['SetTimeStatus']  = ret[2][0][1]
    return retList

# Cnfig设置Specrc特殊资源
def ConfigSetSpecrc(specrc_shutdown, specrc_settime):    
    # 更新
    sql = 'update config set specrc_shutdown = %d, specrc_time = %d where id == 1' % (specrc_shutdown, specrc_settime)
    ret = SqlExecute(sql)
    return ret

def CreateTb_Url():
    global GCUR
    global GDEBUG

    # 创建url表 type:0-白 1-黑
    sql = '''create table if not exists url (
	id integer not null primary key, 
	url char(128) unique,
	type  integer
    );'''

    ret = SqlExecute(sql)
    if ret[0] != 0 :
        return ret

    # 创建配置表
    sql = '''create table if not exists config (
	id integer not null primary key, 
	url_white integer,
	url_black integer,
	device_cdrom integer,
	device_usb integer,
	specrc_shutdown integer,
	specrc_time integer
    );'''
    ret = SqlExecute(sql)
    if ret[0] != 0 :
        return ret

    # 写入默认配置
    sql = '''insert into config (id, url_white, url_black, device_cdrom, device_usb, specrc_shutdown, specrc_time) values (1, 0, 0, 0, 0, 0, 0)'''
    ret = SqlExecute(sql)
    if ret[0] != 0 :
        return ret
    return ret

if __name__ == "__main__":
    cn = Connect()
    CreateTb_Url()
    UrlAdd("www.baidu.com", 0)
    UrlAdd("www.baidu.com1", 0)
    UrlAdd("www.baidu.com2", 0)
    UrlAdd("www.baidu.com3", 0)
    UrlAdd("www.baidu.com4", 0)
    UrlDel("www.baidu.com")
    ret = UrlQuery(0, 0, 2)
    print ret
    if cn != 0:    
        Close(cn)
