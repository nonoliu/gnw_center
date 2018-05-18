#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年7月20日

@author: admin
'''
from flask import Flask,abort,redirect,url_for,render_template,request
from flask_apscheduler import APScheduler
from src.scheduler import *
from src.asyncFun import *
from src.dataCache import dataCache
import logging
from src.urlFun.urlRoute import *
from flask_socketio import SocketIO

#logging.basicConfig(level=logging.ERROR,filename='log/gnw.log')

CACHE = dataCache()

EP = subOB()
app = Flask(__name__)
app.secret_key = config_secret_key
api = Api(app)

api.add_resource(index, '/')
api.add_resource(routeList,'/manager/route')
api.add_resource(serverList,'/manager/server')
api.add_resource(getLogs,'/manager/logs')
api.add_resource(setRouteStatus,'/api/routestatus')
api.add_resource(setServerStatus,'/api/serverstatus')
api.add_resource(changeWatchZone,'/api/changewz')
api.add_resource(addServer,'/api/addserver')
api.add_resource(login,'/login')
api.add_resource(logout,'/logout')
api.add_resource(getNodeList,'/api/nodelist')


#api.add_resource(urlF.setComputerInfo, '/computerinfo/update/test')

#添加收集作业， 每2分钟执行一次
sinit = init()
for _buf in CACHE.routeList:
    Config.JOBS.append({
               'id':_buf[3],  
               'func':'src.asyncFun:asyncPing2',
               'args': ["###".join(_buf)],
               'trigger': {
                    'type': 'cron',
                    'minute':'*/2',
                    'second': '5'
                }
             })
#sss
app.config.from_object(Config())
sinit.addJob(app)

def create_app():
    app = Flask(__name__)
    return app

    
@app.errorhandler(404)
def pageNotFound(error):
    return make_response(EP.p404(), 404,headers)

@app.errorhandler(500)
def postError(error):
    return make_response(EP.p404(), 404,headers)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080,threaded=True)