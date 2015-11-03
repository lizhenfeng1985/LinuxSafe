# -*- coding: utf-8 -*-


import ConfigParser

def ReadConfig():
    configfile = "./config/config_default.ini"
    cfg = ConfigParser.ConfigParser()
    cfg.read(configfile)
    return cfg

def WriteConfig():
    pass

#cfg = ReadConfig()
#print cfg.get("DataBase", "DbName")
