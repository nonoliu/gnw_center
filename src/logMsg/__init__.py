#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2012-10-23

@author: Dongyt 
'''


import logging
from logging.handlers import RotatingFileHandler
import os
from src.config import *


#日志实例化类  
class logMessage(object):
    def __init__(self):  
        #cf = ConfigParser.RawConfigParser()
        _curpath = os.path.split(os.path.realpath(__file__))[0]
        #self._backupLogPath = _curpath + "%s..%slog%scmdbAPI.log"%(os.sep,os.sep,os.sep)
        self._backupLogPath = config_logPath
    
    def initlog(self):
        logger = None
        logger = logging.getLogger()
        #hdlr = logging.FileHandler("kws30.log")
        hdlr = RotatingFileHandler(self._backupLogPath, maxBytes=10*1024*1024,backupCount=5)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.NOTSET)
        return [logger,hdlr]

    def logWirte(self, fun_name, err_msg,level ):
        try:
            message = fun_name + ':'+err_msg
            logger,hdlr = self.initlog()
            logger.log(level ,message )
            hdlr.flush()
            logger.removeHandler( hdlr )
            hdlr.flush()
            hdlr.close()
        except Exception as e:
            print e
