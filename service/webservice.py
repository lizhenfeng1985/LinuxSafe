# -*- coding: utf-8 -*-
import web
import db
import sys
import json

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/url/white/getlist', 'url_white_getlist',
    '/url/white/add',     'url_white_add',
    '/url/white/del',     'url_white_del',
    '/url/black/getlist', 'url_black_getlist',
    '/url/black/add',     'url_black_add',
    '/url/black/del',     'url_black_del',
)


app = web.application(urls, globals())

class index:        
    def GET(self):
        i = web.input()
        print i
        url_whitelist = "lzf"
        return render.index()

class url_white_getlist:        
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
        UrlWhite['ErrStat'] = ret[0]
        UrlWhite['ErrMsg'] = ret[1]
        return render.url_white(json.dumps(UrlWhite))

    def POST(self):
        return self.GET()
    
if __name__ == "__main__":
    if db.Connect() != 0 :
        sys.exit()
    app.run()
