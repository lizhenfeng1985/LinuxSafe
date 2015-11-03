# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import HTMLParser

def Get(url, param):
    param_str = urllib.urlencode(param)
    url_str = "%s?%s" % (url, param_str)
    try:
        req  = urllib2.Request(url_str)
        res  = urllib2.urlopen(req, data=None, timeout=15)
        html = res.read()
        res.close()
        text = HTMLParser.HTMLParser().unescape(html)
        return json.loads(text)
    except Exception as e:
        print ("[Error] http.Get(%s)" % (url_str))
        print (e.message)
        return {'ErrStat':-1,'ErrMsg':e.message}

def Post(url, param):
    param_str = urllib.urlencode(param)
    try:
        req  = urllib2.Request(url)
        res  = urllib2.urlopen(req, data=param_str, timeout=15)
        html = res.read()
        res.close()
        text = HTMLParser.HTMLParser().unescape(html)
        return json.loads(text)
    except Exception as e:
        print ("[Error] http.Get(%s)" % (url))
        print (e.message)
        return {'ErrStat':-1,'ErrMsg':e.message}
    
if __name__ == "__main__":
    url = "http://127.0.0.1:8080/url/white/getlist"
    param = {
        'Start' : 0,
        'Length': 10
    }
    ret = Get(url, param)
    print type(ret)
    print ret

    ret = Post(url, param)
    print type(ret)
    print ret


