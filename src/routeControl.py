#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2018年4月28日

@author: admin
'''
from time import sleep
from src.bgp4 import getRouteInfo
from src.tratto.systems import *
from src.tratto.connectivity import *
import json 
from config import *
import re
from src.logMsg import logMessage
import time
from src.dataCache import dataCache, pingResultQ
import os

LOG = logMessage()
_PINGCOMMAND = ['ping www.baidu.com\n','ping count 4 www.baidu.com\n']

class routeControl(object):
    
    def test(self,test):
        global pingResultQ
        pingResultQ.put("test1111")
        print pingResultQ.qsize()
    
    def getPingValue(self, rinf,_timestamp):
        '''获取路由器ping 结果'''  
        global pingResultQ
        
        try:
            routeInfo = rinf.split('###')
            _result = [{'result':'True','timestamp':_timestamp,'address':routeInfo[3],'lng':routeInfo[8]\
                        ,'lat':routeInfo[9],'ret':[]}]
            self.CACHE = dataCache()
            m = SystemProfiles['IOS']
            s = Session(routeInfo[3],23,"telnet",m)
            if routeInfo[5] == '1':
                s.login('', '')
                for _desAddress in self.CACHE.serverList:
                    try:
                        _buf = self.formatData(s.sendcommand('ping',_desAddress[0]))
                        if _buf['result'] == 1:
                            _bufr = ' '.join((str(_buf['value'][0]),str(_buf['value'][1]),str(_buf['value'][2])))
                            _result[0]['ret'].append({'source':routeInfo[3],'des':_desAddress[0],'result':_bufr,
                                                      'lng':_desAddress[2],'lat':_desAddress[3]})
                    except Exception as e:
                        print e
            else:
                s.login(routeInfo[6],routeInfo[7])
                for _desAddress in self.CACHE.serverList:
                    try:
                        _buf = self.formatData(s.sendcommand('ping',_desAddress[0]))
                        if _buf['result'] == 1:
                            _bufr = ' '.join((str(_buf['value'][0]),str(_buf['value'][1]),str(_buf['value'][2])))
                            _result[0]['ret'].append({'source':routeInfo[3],'des':_desAddress[0],'result':_bufr,
                                                      'lng':_desAddress[2],'lat':_desAddress[3]})
                    except Exception as e:
                        LOG.logWirte('error', 'get ping value:' + str(e), 1)
            s.logout()
        except Exception as e:
            _result[0] = {'result':'False'}
            LOG.logWirte('error', "get ping value :" + str(e) + rinf, 2)
        if len(_result[0]['ret']) == 0 :_result[0]['result'] = 'False'
        pingResultQ.put( _result )
        return _result
    
    def checkRouteList(self):
        '''测试服务器列表，'''
        #抓取最新列表
        _grl = getRouteInfo()
        _list = _grl.getList()
        
        _result = []
        #测试服务器状态， BIRO，Quagga 目前不支持ping 自动屏蔽
        #在服务器列表中识别出需要密码的
        for _buf in _list:
            try:
                _buft = _buf
                if _buf[2] == 'BIRD':
                    _buft[4] = 'nonsupport'
                    _buft.append(False)
                    _result.append(_buft)
                    continue
                elif _buf[2] == 'Quagga':
                    _buft[4] = 'nonsupport'
                    _buft.append(False)
                    _result.append(_buft)
                    continue
                s = Session(_buf[3],23,"telnet",'')
                _rt = s.checkConnect()
                if _rt[0] == 0:
                    _buft[4] = 'nonsupport'
                    _buft.append(_rt[1])
                else:
                    _buft.append(_rt[1])
                _result.append(_buft)
            except Exception as e:
                LOG.logWirte('error', "check route list :" + str(e), 1)
        return _result
    
    def formatData(self,value):
        value = value.split('\r\n')
        _result = {'result':1,'value':'null'}
        try:
            if value[-1] == '{master}':
                _pingValue = value[-3].split('=')
                if len(_pingValue) > 1:
                    _bufv = re.split('/| ',_pingValue[1].strip())
                    #'min:',int(float(_bufv[0])),'avg:',int(float(_bufv[1])),'max:',int(float(_bufv[2]))
                    _result['value'] = (int(float(_bufv[0])),int(float(_bufv[1])),int(float(_bufv[2])))
                else:
                    #_result['result'] = 0
                    _result['value'] = (1000,1000,1000)
                    LOG.logWirte('info', "get ping value :" + str(_pingValue), 1)
            elif value[-1] == "% Invalid input detected at '^' marker.":
                _result['result'] = 0
            else:
                _pingValue = value[-1].split('=')
                if len(_pingValue) > 1:
                    _bufv = re.split('/| ',_pingValue[1].strip())
                    _result['value'] = (int(float(_bufv[0])),int(float(_bufv[1])),int(float(_bufv[2])))
                else:
                    #_result['result'] = 0
                    _result['value'] = (1000,1000,1000)
                    LOG.logWirte('info', "get ping value :" + str(_pingValue), 2)
        except Exception as e:
            _result['result'] = 0
            LOG.logWirte('error', "format data:" + str(e), 1)
        return _result