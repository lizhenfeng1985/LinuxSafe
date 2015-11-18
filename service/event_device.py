# -*- coding: utf-8 -*-

######################
# Filename : event_device.py
#            外部设备消息处理
#
# 1、界面修改设备管理之后，更新这里
# 2、收到内核的消息，这里进行匹配
#######################

import threading
import logdb
import pwd

# 全局变量
global GMUTEX_DEVICE    # 线程锁
global GDEVICECDROMSTAT # CDROM状态 0:关闭 1:开启
global GDEVICEUSBSTAT   # USB状态   0:关闭 1:开启

GDEVICECDROMSTAT = 0
GDEVICEUSBSTAT   = 0
GMUTEX_DEVICE    = threading.Lock()


## 检查CDROM是否允许访问
#  返回值 0允许访问 1不允许访问
def UrlCheckCdrom(uid, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip):
        global GDEVICECDROMSTAT
        global GMUTEX_DEVICE

        ret= 0
        if GMUTEX_DEVICE.acquire(1):
                if GDEVICECDROMSTAT == 1: # CDROM保护开启
                        sql = 'insert into log (id, type, user, subpid, objpid, subproc, objsrcpath, objdstpath, sipdip, status, perm, time) ' + \
                                'values(null, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", datetime())' % ('外设管理-CDROM', \
                                pwd.getpwuid(uid).pw_name, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip, '开启', '拦截')
                        logdb.LogAddOne(sql)
                        ret = 1
                else:
                        ret = 0
                GMUTEX_DEVICE.release()
        return ret

## 检查USB存储设备是否允许访问
#  返回值 0允许访问 1不允许访问
def UrlCheckUsb(uid, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip):
        global GDEVICEUSBSTAT
        global GMUTEX_DEVICE

        ret= 0
        if GMUTEX_DEVICE.acquire(1):
                if GDEVICEUSBSTAT == 1: # USB保护开启
                        sql = 'insert into log (id, type, user, subpid, objpid, subproc, objsrcpath, objdstpath, sipdip, status, perm, time) ' + \
                                'values(null, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", datetime())' % ('外设管理-USB', \
                                pwd.getpwuid(uid).pw_name, sub_pid, obj_pid, sub_pro, obj_src, obj_dst, sip_dip, '开启', '拦截')
                        logdb.LogAddOne(sql)
                        ret = 1
                else:
                        ret = 0
                GMUTEX_DEVICE.release()
        return ret


## 设置状态
#  返回值 0：成功 -1：失败
def DeviceSetStat(cdrom_stat, usb_stat):
        if cdrom_stat not in (0, 1) or usb_stat not in (0, 1):
                return -1
        
        global GDEVICECDROMSTAT
        global GDEVICEUSBSTAT
        global GMUTEX_DEVICE
        if GMUTEX_DEVICE.acquire(1):
                GDEVICECDROMSTAT = cdrom_stat
                GDEVICEUSBSTAT = usb_stat
                GMUTEX_DEVICE.release()
        return 0


