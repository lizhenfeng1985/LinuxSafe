# -*- coding: utf-8 -*-
import web

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/url/white/getlist', 'url_white_getlist',
    '/url/white/add', 'url_white_add',
    '/url/white/del', 'url_white_del',
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
            'Start'   : 0,
            'Lists'   : [],
            'Totle'   : 23,
        }
        
        param = web.input()
        if param.has_key('Start') == False and param.has_key('Length') == False:
            UrlWhiteList['ErrStat'] = -1
            UrlWhiteList['ErrMsg'] = u'缺少参数 param:Start=A&Length=B'
            return render.url_white_list(UrlWhiteList)
            
        start  = int(param['Start'])
        length = int(param['Length'])        
        
        for i in range(start, start + length):
            if i >= 23:
                break
            UrlWhiteList['Lists'].append(u"www.jiangmin.com/%d.html" % (i))
        
        return render.url_white_list(UrlWhiteList)

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
            return render.url_white(UrlWhite)
        return render.url_white(UrlWhite)

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
            return render.url_white(UrlWhite)
        return render.url_white(UrlWhite)
    
if __name__ == "__main__":
    app.run()
