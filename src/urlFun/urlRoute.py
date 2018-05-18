#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年7月20日

@author: admin
'''

from flask import Flask,abort,redirect,url_for,render_template,request,make_response,jsonify,session
#from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import hashlib
import time
from src.config import *
import json
from datetime import datetime,timedelta
from src.urlFun.subFun import subFun
from src.ipip import IPX
import os

parser = reqparse.RequestParser()
parser.add_argument('ss', type=str, help='test')
parser.add_argument('accesstoken', type=str)
parser.add_argument('timestamp', type=int)#, required=True)
parser.add_argument('wanip',type=str)
parser.add_argument('action',type=str)
parser.add_argument('wz',type=str)
parser.add_argument('watch',type=int)
parser.add_argument('agent',type=int)
parser.add_argument('zone',type=str)
parser.add_argument('address',type=str)
parser.add_argument('Lock_tables_priv', type=str,choices=['Y','N'],default='N')
headers = {'Content-Type': 'text/html'}
user_fields = {
    'sid': fields.String
}

#_th = ThreadPool(100)

class pageNotFound(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)

class subOB(object):
    def __init__(self):
        self._errorPage = '<!DOCTYPE html>\
            <html lang="en">\
                <body>\
                    <div class="container not-found">\
                        <div class="row">\
                            <div class="col-lg-12">\
                                <h1>Oops! 404</h1>\
                                <p>not found...</p>\
                            </div>\
                        </div>\
                    </div>\
                        </body>\
            </html>'
    
    def p404(self):
        return self._errorPage
    
    def checkToken(self,_accesstoken,_timestamp):
        _key =  config_URL_KEY
        if _accesstoken == 'asdfasdf23esf23easdf23zfas3':
            return True
        _bufTime = "%d" % time.time()
        _bufKey = hashlib.md5(str(_timestamp) + hashlib.md5(_key).hexdigest()).hexdigest()
        _max = int(time.time() + 1000)
        _min = int(time.time() - 1000)
        _buf = str(_accesstoken).strip()
        if _bufKey == _buf and int(_timestamp) <= _max and int(_timestamp) >= _min:
            return True
        return False
    
    def loginSession(self):
        _result = False
        if session.get('username') != None:
            _result = True
        return _result

class serverHeartbeat(Resource):
    def __init__(self):
        self.subOB = subOB()
        
    @marshal_with(user_fields)
    def get(self,sid=''):
        self.subf
        return make_response(jsonify(self.subf.heartbeat(sid), 200,headers))
    
    def post(self):
        return make_response(self.subOB.p404(), 404,headers)

class login(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        _data= render_template('login.html')
        response = make_response(_data)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    
    def post(self):
        _result = self.subf.checkSession(request.form['username'], request.form['password'])
        if len(_result) != 0:
            session['username']=request.form['username']
        return redirect(url_for('index'))

class logout(Resource):
    def __init__(self):
        self.subOB = subOB()
    
    def get(self):
        session.pop('username',None)
        session.pop('password',None)
        return redirect(url_for('login'))
    
    def post(self):
        return make_response(self.subOB.p404(), 404,headers)

class index(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        if not self.subOB.loginSession():
            return redirect(url_for('login'))
        _online = []
        _offline = []
        _bufServerList = self.subf.getServerList()
        for _buf in _bufServerList:
            if (datetime.now()-_buf[7]).seconds < 3600:
                _online.append({'address':_buf[0],'zone':_buf[3]})
            else:
                _offline.append({'address':_buf[0],'zone':_buf[3]})
        
        data= render_template('index.html',onlinetable=_online,offlinetable=_offline)
        response = make_response(data)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response

class routeList(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        if not self.subOB.loginSession():
            return redirect(url_for('login'))
        _routeList = []
        
        _bufRouteList = self.subf.getRouteList()
        _timestamp = "%d" % time.time()
        _token = hashlib.md5(str(_timestamp) + hashlib.md5(config_URL_KEY).hexdigest()).hexdigest()
        
        for _buf in _bufRouteList:
            _label = 'label-danger'
            if _buf[10] == 'OK':
                _label = 'label-success'
            _routeList.append({'provider':_buf[0],'type':_buf[1],'lng':_buf[2],'lat':_buf[3],'address':_buf[4],'username':_buf[5],
                               'password':_buf[6],'failC':_buf[7],'deleteF':_buf[8],'hb':_buf[9],'status':_buf[10],'label':_label})
        _data= render_template('route.html',table=_routeList,timpstamp=_timestamp,token=_token)
        response = make_response(_data)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    
    def post(self):
        return make_response(self.subOB.p404(), 404,headers)
    
class serverList(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        _serverList = []
        if not self.subOB.loginSession():
            return redirect(url_for('login'))
        
        _bufServerList = self.subf.getServerList()
        _timestamp = "%d" % time.time()
        _token = hashlib.md5(str(_timestamp) + hashlib.md5(config_URL_KEY).hexdigest()).hexdigest()
        
        for _buf in _bufServerList:
            _label = 'label-danger'
            if (datetime.now()-_buf[7]).seconds < 3600:
                _label = 'label-success'
            _serverList.append({'address':_buf[0],'lng':_buf[1],'lat':_buf[2],'izone':_buf[3],'agent':_buf[4],'flag':_buf[5],
                               'zone':_buf[6],'time':_buf[7],'label':_label})
        _data= render_template('server.html',table=_serverList,timpstamp=_timestamp,token=_token)
        response = make_response(_data)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    
    def post(self):
        return make_response(self.subOB.p404(), 404,headers)

class setServerStatus(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)
    
    def post(self):
        args = parser.parse_args()
        _result = {"status":0}
        if not self.subOB.checkToken(args['accesstoken'], args['timestamp']):
            return make_response(jsonify(_result), 403,headers)
        _status = 1
        if args['action'] == 'enable':
            _status = 0
        if self.subf.setServerStatus(_status, args['wanip']):
            _result = {"status":1}
        return make_response(jsonify(_result), 200,headers)

class changeWatchZone(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)
    
    def post(self):
        args = parser.parse_args()
        _result = {"status":0}
        if not self.subOB.checkToken(args['accesstoken'], args['timestamp']):
            return make_response(jsonify(_result), 403,headers)
        _wz = 1
        if args['wz'] == '1':
            _wz = 0
        if self.subf.changeWatchZone(_wz, args['wanip']):
            _result = {"status":1}
        return make_response(jsonify(_result), 200,headers)
    
class addServer(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)
    
    def post(self):
        args = parser.parse_args()
        _result = {"status":0}
        if not self.subOB.checkToken(args['accesstoken'], args['timestamp']):
            return make_response(jsonify(_result), 403,headers)
        _lng = ''
        _lat = ''
        try:
            IPX.load(os.path.abspath("src"+os.sep+"mydata4vipday2.datx"))
            _ipinfo = IPX.find(args['address']).split("\t")
            _lng = _ipinfo[6]
            _lat = _ipinfo[5]
        except Exception as e:
            print e

        if self.subf.addServer(args['address'], _lng, _lat, args['zone'], args['agent'], args['watch']):
            _result = {"status":1}
        return make_response(jsonify(_result), 200,headers)

class setRouteStatus(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)
    
    def post(self):
        args = parser.parse_args()
        _result = {"status":0}
        if not self.subOB.checkToken(args['accesstoken'], args['timestamp']):
            return make_response(jsonify(_result), 403,headers)
        _status = 1
        if args['action'] == 'enable':
            _status = 0
        if self.subf.setRouteStatus(_status, args['wanip']):
            _result = {"status":1}
        return make_response(jsonify(_result), 200,headers)

class getNodeList(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        return make_response(self.subOB.p404(), 404,headers)
    
    def post(self):
        _results = []
        for _buf in self.subf.getAllnodeList():
            _results.append({'address':_buf[0],'lng':_buf[1],'lat':_buf[2]})
        return make_response(jsonify(_results), 200,headers)
    
class getLogs(Resource):
    def __init__(self):
        self.subOB = subOB()
        self.subf = subFun()
        
    def get(self):
        if not self.subOB.loginSession():
            return redirect(url_for('login'))
        _routeList = []
        
        _bufServerList = self.subf.getServerList()
        _timestamp = "%d" % time.time()
        _token = hashlib.md5(str(_timestamp) + hashlib.md5(config_URL_KEY).hexdigest()).hexdigest()
        
        for _buf in _bufServerList:
            _label = 'label-danger'
            if (datetime.now()-_buf[7]).seconds < 3600:
                _label = 'label-success'
            _routeList.append({'address':_buf[0],'lng':_buf[1],'lat':_buf[2],'zone':_buf[3],'agent':_buf[4],'flag':_buf[5],
                               'zone':_buf[6],'time':_buf[7],'label':_label})
        _data= render_template('logs.html',table=_routeList,timpstamp=_timestamp,token=_token)
        response = make_response(_data)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    
    def post(self):
        return make_response(self.subOB.p404(), 404,headers)