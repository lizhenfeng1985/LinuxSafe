# -*- coding: utf-8 -*-


import config
import sqlite3
import os


def Connect():
    cfg = config.ReadConfig()
    try:
        dbname = cfg.get("DataBase", "DbName")
    except:
        print "Err:config.get(DataBase, DbName)"
        return None
    
    try:
        con = sqlite3.connect(dbname)
    except:
        print "Err:sqlite3.connect(%s)" % (dbname)
        return None

    return con
    
def Close(con):
    con.close()
    
#cn = Connect()
#if cn != None:    
#    Close(cn)
