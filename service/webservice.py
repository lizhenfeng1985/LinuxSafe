# -*- coding: utf-8 -*-
import web
import db
import sys
import json
import event_srv
import event_url
import event_device
import event_specrc
import threading
from service_url import *
from service_device import *
from service_specrc import *


render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/url/white/getlist', 'url_white_getlist',
    '/url/white/add',     'url_white_add',
    '/url/white/del',     'url_white_del',
    '/url/black/getlist', 'url_black_getlist',
    '/url/black/add',     'url_black_add',
    '/url/black/del',     'url_black_del',
    '/config/get',        'config_get',
    '/config/set',        'config_set',
    '/config/getdevice',  'config_get_device',
    '/config/setdevice',  'config_set_device',
    '/config/getspecrc',  'config_get_specrc',
    '/config/setspecrc',  'config_set_specrc',
)


app = web.application(urls, globals())

class index:        
    def GET(self):
        i = web.input()
        print i
        url_whitelist = "lzf"
        return render.index()

# 初始化URL
def InitUrl():
    # 配置
    ret = db.ConfigGet()
    if ret['ErrStat'] != 0:
        print ret['ErrMsg']
        return ret[0]
    event_url.UrlSetStat(ret['Config']['White_Start'], ret['Config']['Black_Start'])

    # 白名单
    ret = db.UrlQuery(0, 0, 65535)
    if ret['ErrStat'] != 0:
        print ret['ErrMsg']
        return ret[ErrStat]
    for url in ret['Lists']:
        event_url.UrlAddWhite(url)

    # 黑名单
    ret = db.UrlQuery(1, 0, 65535)
    if ret['ErrStat'] != 0:
        print ret['ErrMsg']
        return ret[ErrStat]
    for url in ret['Lists']:
        event_url.UrlAddBlack(url)
    return 0

# 初始化Device
def InitDevice():
    # 配置
    ret = db.ConfigGetDevice()
    if ret['ErrStat'] != 0:
        print ret['ErrMsg']
        return ret[0]
    
    event_device.DeviceSetStat(ret['Config']['CdromStatus'], ret['Config']['UsbStatus'])
    return 0

# 初始化特殊资源
def InitSpecrc():
    # 配置
    ret = db.ConfigGetSpecrc()
    if ret['ErrStat'] != 0:
        print ret['ErrMsg']
        return ret[0]
    
    event_specrc.SpecrcSetStat(ret['Config']['ShutDownStatus'], ret['Config']['SetTimeStatus'])
    return 0

if __name__ == "__main__":
    if db.Connect() != 0 :
        sys.exit()

    # url初始化
    InitUrl()

    # 初始化Device
    InitDevice()

    # 初始化Specrc
    InitSpecrc()

    # 启动消息处理服务
    server = event_srv.EpollServer(host="localhost", port=7000)
    t_event = threading.Thread(target=server.run, args=())
    t_event.start()
    
    app.run()
