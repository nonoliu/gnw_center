#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''

from src.config import *
import json
from src.cacheDump import *
import Queue

routeList = None
serverList = None
failStat = {}
pingResultQ = Queue.Queue(10000)


'''
全局变量，缓存各种全局信息
'''
class dataCache(object):
    def __init__(self):
        self._groupInfo = None
        self._cacheDump = cacheDump()
        global config
        

    @property
    def routeList(self):
        global routeList
        try:
            if routeList == None:
                routeList = self._cacheDump.cacheLoad('routeList')
        except:
            pass
        return routeList
    
    @routeList.setter
    def routeList(self,value):
        global routeList
        routeList = value
        self._cacheDump.cacheSave('routeList', value)

    @property
    def failStat(self):
        global failStat
        try:
            if failStat == None:
                failStat = self._cacheDump.cacheLoad('failStat')
        except:
            pass
        return failStat
    
    @failStat.setter
    def failStat(self,value):
        global failStat
        failStat = value
        self._cacheDump.cacheSave('failStat', value)
    
    @property
    def serverList(self):
        global serverList
        try:
            if serverList == None:
                serverList = self._cacheDump.cacheLoad('serverList')
        except:
            pass
        return serverList
    
    @serverList.setter
    def serverList(self,value):
        global serverList
        serverList = value
        self._cacheDump.cacheSave('serverList', value)
        
    
    
    def modifyList(self,_list,_key,_value):
        _i = len(_list)
        for _buf in range(0,_i):
            if _list[_buf]['type'] == _key:
                _list[_buf]['value']=_list[_buf]['value']+_value
                break
        return _list
        
