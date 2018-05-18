#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''
import os
import json

#缓存落地
class cacheDump(object):
    def __init__(self):
        self._cachePath = os.getcwd() + os.sep + "tmp" + os.sep
    
    def cacheSave(self,name,value):
        if not os.path.exists(self._cachePath):
            os.makedirs(self._cachePath)
        with open(self._cachePath + name,'w+' ) as _f:
                json.dump(value,_f)
    
    def cacheLoad(self,name):
        _dJson = None
        with open(self._cachePath + name, "r") as _f:
            _dJson = json.load(_f)
        return _dJson
