#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
Created on 2017年11月6日

@author: admin
'''
try:
    import fcntl
except:
    pass
import atexit

from flask_apscheduler import APScheduler


class Config(object):  
    JOBS = [
            {
               'id':'syncRouteList',  
               'func':'src.asyncFun:syncRouteList',
               'args': '',
               'trigger': {
                    'type': 'cron',
                    #'day_of_week':"mon-fri",
                    'hour':'2',
                    'minute':'1',
                    #'minute':'0-11',
                    'second': '5'  
                    #'second': '*/5'  
                }
            },
            {
               'id':'getPingValue',  
               'func':'src.asyncFun:getPingValue',
               'args': '',
               'trigger': {
                    'type': 'cron',
                    'minute':'*/2',
                    #'minute':'0-11',
                    'second': '59'  
                    #'second': '*/5'  
                }
            },
            {
               'id':'syncServerStatus',  
               'func':'src.asyncFun:syncServerStatus',
               'args': '',
               'trigger': {
                    'type': 'cron',
                    'hour':'*/2',
                    'minute':'1',
                    #'minute':'0-11',
                    'second': '59'  
                    #'second': '*/5'  
                }
            },
            {
               'id':'syncServerList',  
               'func':'src.asyncFun:syncServerList',
               'args': '',
               'trigger': {
                    'type': 'cron',
                    #'day_of_week':"mon-fri",
                    'hour':'*/2',
                    'minute':'30',
                    #'minute':'0-11',
                    'second': '5'  
                    #'second': '*/5'  
                }
            }#,
            #{syncServerStatus
             #  'id':'asyncPing',  
             #  'func':'src.asyncFun:asyncPing',
             ##  'args': '',
             #  'trigger': {
             #       'type': 'cron',
                    #'day_of_week':"mon-fri",
                    #'hour':'*/2',
             #       'minute':'*/5',
                    #'minute':'0-11',
                    #'second': '5'  
                    #'second': '*/5'  
              #  }
             #}
        ]
         
    SCHEDULER_API_ENABLED = True

class init(object):
    def __init__(self):
        pass
    
    def addJob(self,scinit):
        f = open("scheduler.lock", "wb")
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler = APScheduler()
            scheduler.init_app(scinit)
            #for _buf in CACHE.routeList:
            #    scheduler.add_job(id=_buf[3], func='src.asyncFun:asyncPing2',args="###".join(_buf),trigger={'type': 'cron','minute':'*/5','second': '5'})
            scheduler.start()
        except Exception as e:
            print e
        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()
        atexit.register(unlock)
