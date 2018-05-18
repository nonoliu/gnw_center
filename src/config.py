#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''

config_updateURL = "http://0.0.0.0:5012/computerinfo/update/test"
config_URL_KEY = 'youselfdefine'
config_lockTime = 3600
config_es = "ping.es.???.com:80"
config_logPath = "D:\workspace\globalNetworkWatch_center\src\log\cmdbAPI.log"
config_secret_key = "\xf2\x91Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96"
lockList = {}
config_connKwargs = {'host':'111.11.1.1','user':'gnw_user', 'passwd':'11111', 'db':'gnw_center', 'charset':"utf8" ,'port':3306}
config_routeAuth = {'286':{'Username':'rs','Password':'loveAS286','finish':'>'},'3257':{'login':'public','Password':'public','finish':'>'},'3741':{'Username':'rviews','Password':'rviews','finish':'>'},
                '4589':{'login':'public','Password':'Public','finish':'>'},'5713':{'Username':'saix','Password':'saix','finish':'>'},'6447':{'Username':'rviews','Password':'','finish':'>'},
                '7018':{'login':'rviews','Password':'rviews','finish':'>'},'7920':{'Username':'rviews','Password':'','finish':'>'},'15290':{'Username':'rserv','Password':'','finish':'>'},
                '15763':{'login':'','Password':'','finish':'#'}}