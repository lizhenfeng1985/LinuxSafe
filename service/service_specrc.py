# -*- coding: utf-8 -*-
import web
import db
import sys
import json
import event_specrc

render = web.template.render('templates/')


class config_get_specrc:        
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Config'  : {}
        }
        
        ConfigData = db.ConfigGetSpecrc()        
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()

class config_set_specrc:
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('ShutDownStatus') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:ShutDownStatus=status'
            return render.config(json.dumps(ConfigData))
        if param.has_key('SetTimeStatus') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:SetTimeStatus=status'
            return render.config(json.dumps(ConfigData))
        
        try:
            ShutDownStatus = int(param['ShutDownStatus'])
            SetTimeStatus  = int(param['SetTimeStatus'])
        except:
            onfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = "Failed:param value err"
            return render.config(json.dumps(ConfigData))
        
        ret = db.ConfigSetSpecrc(ShutDownStatus, SetTimeStatus)
        if ret[0] == 0:
            event_specrc.SpecrcSetStat(ShutDownStatus, SetTimeStatus)
        ConfigData['ErrStat'] = ret[0]
        ConfigData['ErrMsg'] = ret[1]
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()
