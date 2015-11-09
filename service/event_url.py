# -*- coding: utf-8 -*-

######################
# Filename : event_url.py
#            URL消息处理
#
# 1、界面修改url之后，更新这里
# 2、收到内核的消息，这里进行匹配
#######################

import threading

# 全局变量
global GMUTEX_URL      # 线程锁
global GURLDIC         # URL词典
global GURLWHITESTAT   # URL白名单状态 0:关闭 1:开启
global GURLBLACKSTAT   # URL黑名单状态 0:关闭 1:开启

GURLDIC = {}  # url : type (type=0 白名单 type=1 黑名单)
GURLWHITESTAT = 0
GURLBLACKSTAT = 1
GMUTEX_URL    = threading.Lock()

## 添加白名单URL
#  返回值 0：成功 -1：失败
def UrlAddWhite(url):
        global GMUTEX_URL
        global GURLDIC
        
        if GMUTEX_URL.acquire(1):
                GURLDIC[url] = 0
                GMUTEX_URL.release()
        return 0
        
## 添加黑名单URL
#  返回值 0：成功 -1：失败
def UrlAddBlack(url):
        global GMUTEX_URL
        global GURLDIC
        
        if GMUTEX_URL.acquire(1):
                GURLDIC[url] = 1
                GMUTEX_URL.release()
        return 0

## 删除URL
#  返回值 0：成功 -1：失败
def UrlDel(url):
        global GMUTEX_URL
        global GURLDIC

        ret = 0
        if GMUTEX_URL.acquire(1):
                if GURLDIC.has_key(url):
                        del GURLDIC[url]
                else:
                        ret = -1
                GMUTEX_URL.release()
        return ret

## 检查URL是否允许访问
#  返回值 0允许访问 1不允许访问
def UrlCheck(url):
        global GMUTEX_URL
        global GURLDIC
        global GURLWHITESTAT
        global GURLBLACKSTAT
        
        if GMUTEX_URL.acquire(1):
                bHasUrl = GURLDIC.has_key(url)
                urlType = 1
                
                if bHasUrl:
                        urlType = GURLDIC[url]
                
                if GURLWHITESTAT == 1: # 白名单开启
                        if bHasUrl == True and urlType == 0:
                                ret = 0
                        else:
                                ret = 1
                elif GURLBLACKSTAT == 1: # 黑名单开启
                        if bHasUrl == True and urlType == 1:
                                ret = 1
                        else:
                                ret = 0                        
                GMUTEX_URL.release()
        return ret

## 设置URL黑白名单状态
#  返回值 0：成功 -1：失败
def UrlSetStat(white_stat, black_stat):
        if white_stat not in (0, 1) or black_stat not in (0, 1):
                return -1
        
        global GMUTEX_URL
        global GURLWHITESTAT
        global GURLBLACKSTAT
        if GMUTEX_URL.acquire(1):
                GURLWHITESTAT = white_stat
                GURLBLACKSTAT = black_stat
                GMUTEX_URL.release()
        return 0


