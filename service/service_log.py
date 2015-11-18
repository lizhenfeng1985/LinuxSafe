# -*- coding: utf-8 -*-
import web
import logdb
import sys
import json
import event_specrc

render = web.template.render('templates/')

class log_url_query:
    def GET(self):
        LogList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 0,
        }
        
        param = web.input()
        if param.has_key('Length') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Length=Length'
            return render.config(json.dumps(LogList))
        if param.has_key('Start') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Start=Start'
            return render.config(json.dumps(LogList))
        if param.has_key('StartTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StartTime=StartTime'
            return render.config(json.dumps(LogList))
        if param.has_key('StopTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StopTime=StopTime'
            return render.config(json.dumps(LogList))
        if param.has_key('KeyWord') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:KeyWord=KeyWord'
            return render.config(json.dumps(LogList))

        print param
        start  = int(param['Start'])
        length = int(param['Length'])
        startTime = param['StartTime']
        stopTime = param['StopTime']
        keyWord = param['KeyWord']

        LogList = logdb.LogUrlQuery(start, length, startTime, stopTime, keyWord)        
        return render.log_list(json.dumps(LogList))
    
    def POST(self):
        return self.GET()

class log_specrc_query:
    def GET(self):
        LogList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 0,
        }
        
        param = web.input()
        if param.has_key('Length') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Length=Length'
            return render.config(json.dumps(LogList))
        if param.has_key('Start') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Start=Start'
            return render.config(json.dumps(LogList))
        if param.has_key('StartTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StartTime=StartTime'
            return render.config(json.dumps(LogList))
        if param.has_key('StopTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StopTime=StopTime'
            return render.config(json.dumps(LogList))
        if param.has_key('KeyWord') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:KeyWord=KeyWord'
            return render.config(json.dumps(LogList))

        print param
        start  = int(param['Start'])
        length = int(param['Length'])
        startTime = param['StartTime']
        stopTime = param['StopTime']
        keyWord = param['KeyWord']

        LogList = logdb.LogSpecrcQuery(start, length, startTime, stopTime, keyWord)        
        return render.log_list(json.dumps(LogList))
    
    def POST(self):
        return self.GET()


class log_device_query:
    def GET(self):
        LogList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 0,
        }
        
        param = web.input()
        if param.has_key('Length') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Length=Length'
            return render.config(json.dumps(LogList))
        if param.has_key('Start') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:Start=Start'
            return render.config(json.dumps(LogList))
        if param.has_key('StartTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StartTime=StartTime'
            return render.config(json.dumps(LogList))
        if param.has_key('StopTime') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:StopTime=StopTime'
            return render.config(json.dumps(LogList))
        if param.has_key('KeyWord') == False:
            ConfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = u'缺少参数 param:KeyWord=KeyWord'
            return render.config(json.dumps(LogList))

        start  = int(param['Start'])
        length = int(param['Length'])
        startTime = param['StartTime']
        stopTime = param['StopTime']
        keyWord = param['KeyWord']

        LogList = logdb.LogDeviceQuery(start, length, startTime, stopTime, keyWord)
        return render.log_list(json.dumps(LogList))
    
    def POST(self):
        return self.GET()
