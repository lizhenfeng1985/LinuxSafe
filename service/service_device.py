# -*- coding: utf-8 -*-
import web
import db
import sys
import json
import event_device

render = web.template.render('templates/')


class config_get_device:        
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Config'  : {}
        }
        
        ConfigData = db.ConfigGetDevice()        
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()

class config_set_device:
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('CdromStatus') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:CdromStatus=status'
            return render.config(json.dumps(ConfigData))
        if param.has_key('UsbStatus') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:UsbStatus=status'
            return render.config(json.dumps(ConfigData))
        
        try:
            cdromStat = int(param['CdromStatus'])
            usbStat   = int(param['UsbStatus'])
        except:
            onfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = "Failed:param value err"
            return render.config(json.dumps(ConfigData))
        
        ret = db.ConfigSetDevice(cdromStat, usbStat)
        if ret[0] == 0:
            event_device.DeviceSetStat(cdromStat, usbStat)
        ConfigData['ErrStat'] = ret[0]
        ConfigData['ErrMsg'] = ret[1]
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()
