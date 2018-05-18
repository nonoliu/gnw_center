#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2018年5月16日

@author: admin
'''

import time
from src.mydb import SwitchDb as mydb
from src.logMsg import logMessage

class subFun(object):
    def __init__(self):
        self.LM = logMessage()
        self.DB = mydb()
        
    def heartbeat(self,_ip):
        _results = {"status":0}
        try:
            _timeCode = time.strftime('%Y%m%d',time.localtime(time.time()))
            if self.DB.modify("UPDATE gnw_serverlist SET hbtime=NOW() WHERE \
            serverAddress='%s'" %(_ip)):
                _results={"status":1}
        except Exception as e:
            self.logWirte('error',"subFun heart beat error: %s" % e,1)
        return _results
    
    def getRouteList(self):
        _results = "0"
        try:
            _results = self.DB.select('SELECT `provider`,`serverType`,`lng`,`lat`,`serverAddress`,`username`,`passwd`\
                            ,`failCount`,`deleteFlag`,`hbtime`,`serverStatus` FROM `gnw_routelist`')
        except Exception as e:
            self.logWirte('error',"subFun ROUTE LIST error: %s" % e,1)
        return _results
    
    def getServerList(self):
        _results = "0"
        try:
            _results = self.DB.select('SELECT `serverAddress`,`lng`,`lat`,`zone`,`isAgent`,`deleteFlag`,`watchZone`,\
                            `hbTime` FROM `gnw_serverlist`')
        except Exception as e:
            self.logWirte('error',"subFun SERVER LIST error: %s" % e,1)
        return _results
    
    def getAllnodeList(self):
        _results = "0"
        try:
            _results = self.DB.select('SELECT serverAddress,lng,lat FROM `gnw_routelist` WHERE deleteFlag = 0\
                                     UNION ALL\
                                    SELECT serverAddress,lng,lat FROM `gnw_serverlist` WHERE deleteFlag = 0;')
        except Exception as e:
            self.logWirte('error',"subFun all node LIST error: %s" % e,1)
        return _results
    
    def setServerStatus(self,_status,_ip):
        _result = {"status":0}
        try:
            if self.DB.modify("UPDATE `gnw_serverlist` SET `deleteFlag` = %d WHERE serverAddress='%s'" 
                              %(_status,_ip)):
                _results={"status":1}
        except Exception as e:
            self.logWirte('error',"set server status error: %s" % e,1)
        return _result
    
    def changeWatchZone(self,_wz,_ip):
        _result = {"status":0}
        try:
            if self.DB.modify("UPDATE `gnw_serverlist` SET `watchZone` = %d WHERE serverAddress='%s'" 
                              %(_wz,_ip)):
                _results={"status":1}
        except Exception as e:
            self.logWirte('error',"set server status error: %s" % e,2)
        return _result
    
    def setRouteStatus(self,_status,_ip):
        _result = {"status":0}
        try:
            if self.DB.modify("UPDATE `gnw_routelist` SET `deleteFlag` = %d WHERE serverAddress='%s'" 
                              %(_status,_ip)):
                _results={"status":1}
        except Exception as e:
            self.logWirte('error',"set route status error: %s" % e,1)
        return _result
    
    def addServer(self,_address,_lng,_lat,_zone,_isAgent,_watchZone):
        _result = {"status":0}
        try:
            if self.DB.modify("CALL `sp_addServerList`('%s','%s','%s','%s',%d,%d)" 
                              %(_address,_lng,_lat,_zone,_isAgent,_watchZone)):
                _results={"status":1}
        except Exception as e:
            self.logWirte('error',"add server error: %s" % e,1)
        return _result
    
    def checkSession(self,_username,_pwd):
        _results = []
        try:
            _results = self.DB.select("SELECT 1 FROM `gnw_users` WHERE username = '%s' AND pwd=PASSWORD('%s')" %(_username,_pwd))
        except Exception as e:
            self.logWirte('error',"check session error: %s" % e,1)
        return _results