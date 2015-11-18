# -*- coding: utf-8 -*-

######################
# Filename : event_specrc.py
#            特殊资源消息处理
#
# 1、界面修改特殊资源管理之后，更新这里
# 2、收到内核的消息，这里进行匹配
#######################

import threading
import logdb
import time
import pwd

# 全局变量
global GMUTEX_SPECRC       # 线程锁
global GSPECRCSHUTDOWNSTAT # CDROM状态 0:关闭 1:开启
global GSPECRCSETTIMESTAT  # USB状态   0:关闭 1:开启

GSPECRCSHUTDOWNSTAT = 0
GSPECRCSETTIMESTAT   = 0
GMUTEX_SPECRC    = threading.Lock()


## 检查关机操作是否允许访问
#  返回值 0允许访问 1不允许访问
def SpecrcCheckShutDown(uid, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip):
        global GSPECRCSHUTDOWNSTAT
        global GMUTEX_SPECRC

        ret= 0
        if GMUTEX_SPECRC.acquire(1):
                if GSPECRCSHUTDOWNSTAT == 1: # 关机保护开启
                        sql = 'insert into log (id, type, user, subpid, objpid, subproc, objsrcpath, objdstpath, sipdip, status, perm, time) ' + \
                                'values(null, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", datetime())' % ('特殊资源-关机', \
                                pwd.getpwuid(uid).pw_name, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip, '开启', '拦截')
                        logdb.LogAddOne(sql)
                        ret = 1
                else:
                        ret = 0
                GMUTEX_SPECRC.release()
        return ret

## 检查设置时间操作是否允许访问
#  返回值 0允许访问 1不允许访问
def SpecrcCheckSetTime(uid, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip):
        global GSPECRCSETTIMESTAT
        global GMUTEX_SPECRC

        ret= 0
        if GMUTEX_SPECRC.acquire(1):
                if GSPECRCSETTIMESTAT == 1: # 时间保护开启
                        ret = 1
                        try:
                                tm1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(obj_src)))
                                tm2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(obj_dst)))
                                tm = "%s -> %s" % (tm1, tm2)
                                sql = 'insert into log (id, type, user, subpid, objpid, subproc, objsrcpath, objdstpath, sipdip, status, perm, time) ' + \
                                        'values(null, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", datetime())' % ('特殊资源-时间', \
                                        pwd.getpwuid(uid).pw_name, sub_pid, obj_pid, sub_pro, tm, '', sip_dip, '开启', '拦截')
                                logdb.LogAddOne(sql)
                        except:
                                pass
                else:
                        ret = 0
                GMUTEX_SPECRC.release()
        return ret


## 设置状态
#  返回值 0：成功 -1：失败
def SpecrcSetStat(shutdown_stat, settime_stat):
        if shutdown_stat not in (0, 1) or settime_stat not in (0, 1):
                return -1
        
        global GSPECRCSHUTDOWNSTAT
        global GSPECRCSETTIMESTAT
        global GMUTEX_SPECRC
        if GMUTEX_SPECRC.acquire(1):
                GSPECRCSHUTDOWNSTAT = shutdown_stat
                GSPECRCSETTIMESTAT  = settime_stat
                GMUTEX_SPECRC.release()
        return 0


