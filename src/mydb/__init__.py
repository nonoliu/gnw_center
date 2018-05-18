#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 2012-10-23

@author: ly 
'''


import pymysql
import logging  
import os
from src.config import *
from src.DBUtils.PooledDB import PooledDB
from src.logMsg import logMessage

class DbManager(object):
    def __init__(self):
        connKwargs = config_connKwargs
        self._pool = PooledDB(pymysql, mincached=0, maxcached=10, maxshared=10, maxusage=1000, **connKwargs)

    def getConn(self):  
        return self._pool.connection()
         
_dbManager = DbManager()  
_logMsg = logMessage()

class SwitchDb(object):

    def __init__(self):
        '''
        Constructor
        '''

    def getConn(self):  
       return _dbManager.getConn()  
           
    def modify (self,sql):
        res=()
        try: 
            #_conn=MySQLdb.connect(host='115.182.1.191',user='net_map',passwd=_pw,port=3306)
            _conn = self.getConn()  
            cur = _conn.cursor()
            res = cur.execute(sql)
            _conn.commit()
            cur.close()
            _conn.close() 
        except Exception as e:
            _logMsg.logWirte('error',"db error: %s (%d)" % (str(e) + "#" +sql,1),1)
            
        return res
    

    def returnInsert(self,sql):
        res=((0,),)
        try: 
            #_conn=MySQLdb.connect(host='115.182.1.191',user='net_map',passwd=_pw,port=3306)
            _conn = self.getConn()  
            cur = _conn.cursor()
            cur.execute(sql)
            cur.execute("select LAST_INSERT_ID();")
            res = cur.fetchall()
            _conn.commit()
            cur.close()
            _conn.close()
        except Exception as e:
            #self.log.error(e)
            _logMsg.logWirte('error',"db error: %d (%d)" % (str(e)+"#" +sql,1),2)
        return res
    
    def select(self,sql):
        res =()
        try:
            #_conn=MySQLdb.connect(host='115.182.1.191',user='net_map',passwd=_pw,port=3306)
            _conn = self.getConn()  
            cur = _conn.cursor()
            cur.execute("set names utf8")
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            _conn.close()
        except Exception as e:
            #self.log.error(e)
            _logMsg.logWirte('error',"db error: %s (%d)" % (str(e)+"#" +sql,1),3)  
        return res
    
#    def closeDb(self):
#        _conn.close()