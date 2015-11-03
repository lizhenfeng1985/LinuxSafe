# -*- coding: utf-8 -*-
import web
import db
import sys
import json
from service_url import *

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
)


app = web.application(urls, globals())

class index:        
    def GET(self):
        i = web.input()
        print i
        url_whitelist = "lzf"
        return render.index()

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
               
        return render.config(json.dumps(ConfigData))
    
    def POST(self):
        return self.GET()
    
if __name__ == "__main__":
    if db.Connect() != 0 :
        sys.exit()
    app.run()
