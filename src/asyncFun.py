#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''

from mydb import SwitchDb as mydb
from src.logMsg import logMessage
from src.routeControl import routeControl
from src.dataCache import dataCache, pingResultQ
from src.subThreads import *
from src.esQuery import esQuery
import time
import platform
import os
from ipip import IPX
import socket


TH = ThreadPool(100)
LOG = logMessage()
CACHE = dataCache()
RC = routeControl()
ES = esQuery()

def syncRouteList():
    try:
        #抓取最新数据，但是没有密码
        IPX.load(os.path.abspath("src"+os.sep+"mydata4vipday2.datx"))
        _mydb = mydb()
        if platform.system() != 'Windows':
            _rc = routeControl()
            _routeList = _rc.checkRouteList()
        
            for _buf in _routeList:
                if len(_buf) == 6:
                    _bufip = socket.gethostbyname(_buf[3])
                    _ipinfo = IPX.find(_bufip).split("\t")
                    _sql = "call sp_setRouteList('%s','%s','%s','%s','%s','%s',0,'%s','%s');" %(_buf[0],\
                                _buf[1],_buf[2],_buf[3],_buf[4],str(_buf[5]).upper(),_ipinfo[6],_ipinfo[5]) 
                    _mydb.modify(_sql)
        #从数据库中取出列表，并放到cache中
        _bufList = _mydb.select('SELECT asn,provider,serverType,serverAddress,serverStatus,useLogin,username,passwd,lng,lat \
                                FROM `gnw_routelist` WHERE failCount < 1000 AND deleteFlag=0;')
        CACHE.routeList = _bufList
        
    except Exception as e:
        LOG.logWirte('error', "sync route list:" + str(e), 1)

#同步agent 服务器列表
def syncServerList():
    try:
        _mydb = mydb()
        _bufList = _mydb.select('SELECT serverAddress,zone,lng,lat FROM gnw_serverList WHERE deleteFlag=0')
        CACHE.serverList = _bufList
    except Exception as e:
        LOG.logWirte('error', "sync server list" + str(e),1)

#异步ping 模块
def asyncPing():
    global pingResultQ
    _timestamp = time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime())
    time.sleep(1)
    for _buf in CACHE.routeList:
        try:
            TH.add_job(RC.getPingValue,"###".join(_buf),_timestamp)
            time.sleep(0.5)
        except Exception as e:
            LOG.logWirte('error', 'async ping1:' + str(e), 1)
    TH.wait_for_complete()

#同步ping 结果到 ES
def getPingValue():
    ES.dataInputES()

#同步服务器状态，
def syncServerStatus():
    try:
        _mydb = mydb()
        if len(CACHE.failStat) != 0:
            for _item in CACHE.failStat:
                _sql = "UPDATE gnw_routelist SET failCount=%d WHERE serverAddress='%s';" %(CACHE.failStat[_item],_item)
                _mydb.modify(_sql)
    except Exception as e:
        LOG.logWirte('error', 'sync server status' + str(e), 1)

#异步ping
def asyncPing2(_rinfo):
    try:
        global pingREsultQ
        _timestamp = time.strftime("%Y-%m-%d %H:%M" ,time.localtime())
        RC.getPingValue(_rinfo,_timestamp)
    except Exception as e:
        LOG.logWirte('error', 'async ping2:' + str(e), 1)
