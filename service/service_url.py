# -*- coding: utf-8 -*-
import web
import db
import sys
import json
import event_url

render = web.template.render('templates/')

class url_white_getlist:        
    def GET(self):
        UrlWhiteList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 0,
        }
        
        param = web.input()
        if param.has_key('Start') == False or param.has_key('Length') == False:
            UrlWhiteList['ErrStat'] = -1
            UrlWhiteList['ErrMsg'] = u'缺少参数 param:Start=A&Length=B'
            return render.url_white_list(json.dumps(UrlWhiteList))
            
        start  = int(param['Start'])
        length = int(param['Length'])        

        UrlWhiteList = db.UrlQuery(0, start, length)        
        return render.url_white_list(json.dumps(UrlWhiteList))
    
    def POST(self):
        return self.GET()
    
class url_white_add:        
    def GET(self):
        UrlWhite = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('Url') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:Url=url'
            return render.url_white(json.dumps(UrlWhite))
        
        ret = db.UrlAdd(param['Url'], 0)
        if ret[0] == 0:
            event_url.UrlAddWhite(param['Url'])
        UrlWhite['ErrStat'] = ret[0]
        UrlWhite['ErrMsg'] = ret[1]
        return render.url_white(json.dumps(UrlWhite))
    
    def POST(self):
        return self.GET()

class url_white_del:        
    def GET(self):
        UrlWhite = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('Url') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:Url=url'
            return render.url_white(json.dumps(UrlWhite))
        
        ret = db.UrlDel(param['Url'])
        if ret[0] == 0:
            event_url.UrlDel(param['Url'])
        UrlWhite['ErrStat'] = ret[0]
        UrlWhite['ErrMsg'] = ret[1]
        return render.url_white(json.dumps(UrlWhite))

    def POST(self):
        return self.GET()

class url_black_getlist:        
    def GET(self):
        UrlWhiteList = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Lists'   : [],
            'Totle'   : 23,
        }
        
        param = web.input()
        if param.has_key('Start') == False and param.has_key('Length') == False:
            UrlWhiteList['ErrStat'] = -1
            UrlWhiteList['ErrMsg'] = u'缺少参数 param:Start=A&Length=B'
            return render.url_white_list(json.dumps(UrlWhiteList))
            
        start  = int(param['Start'])
        length = int(param['Length'])        

        UrlWhiteList = db.UrlQuery(1, start, length)        
        return render.url_white_list(json.dumps(UrlWhiteList))
    
    def POST(self):
        return self.GET()
    
class url_black_add:        
    def GET(self):
        UrlWhite = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('Url') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:Url=url'
            return render.url_white(json.dumps(UrlWhite))
        
        ret = db.UrlAdd(param['Url'], 1)
        if ret[0] == 0:
            event_url.UrlAddBlack(param['Url'])
        UrlWhite['ErrStat'] = ret[0]
        UrlWhite['ErrMsg'] = ret[1]
        return render.url_white(json.dumps(UrlWhite))
    
    def POST(self):
        return self.GET()

class url_black_del:        
    def GET(self):
        UrlWhite = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('Url') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:Url=url'
            return render.url_white(json.dumps(UrlWhite))
        
        ret = db.UrlDel(param['Url'])
        if ret[0] == 0:
            event_url.UrlDel(param['Url'])
        UrlWhite['ErrStat'] = ret[0]
        UrlWhite['ErrMsg'] = ret[1]
        return render.url_white(json.dumps(UrlWhite))

    def POST(self):
        return self.GET()

class config_get:        
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
            'Config'  : {}
        }
        
        ConfigData = db.ConfigGet()        
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()

class config_set:
    def GET(self):
        ConfigData = {
            'ErrStat' : 0,
            'ErrMsg'  : "OK",
        }
        
        param = web.input()
        if param.has_key('WhiteStatus') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:WhiteStatus=status'
            return render.config(json.dumps(ConfigData))
        if param.has_key('BlackStatus') == False:
            UrlWhite['ErrStat'] = -1
            UrlWhite['ErrMsg'] = u'缺少参数 param:BlackStatus=status'
            return render.config(json.dumps(ConfigData))
        
        try:
            wstat = int(param['WhiteStatus'])
            bstat = int(param['BlackStatus'])
        except:
            onfigData['ErrStat'] = -1
            ConfigData['ErrMsg'] = "Failed:param value err"
            return render.config(json.dumps(ConfigData))
        
        ret = db.ConfigSet(wstat, bstat)
        if ret[0] == 0:
            event_url.UrlSetStat(wstat, bstat)
        ConfigData['ErrStat'] = ret[0]
        ConfigData['ErrMsg'] = ret[1]
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()
