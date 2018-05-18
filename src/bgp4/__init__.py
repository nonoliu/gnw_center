#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''

import urllib2
from bs4 import BeautifulSoup

class getRouteInfo(object):

    '''
    get route list
    default init parameter, url:bgp4
    eg:
         _rl = getRouteInfo() 
         or 
         _rl = getRouteInfo('http://baidu.com/1111')
    '''
    def __init__(self, url='https://www.bgp4.net/doku.php?id=tools:ipv4_route_servers'):
        self._bgp4URL=url
    
    #get html value, return route list, type is list
    def getList(self):
        #默认值
        _value = 'Flase'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        request = urllib2.Request(self._bgp4URL, headers=headers)
        response = urllib2.urlopen(request)
        response.encoding = 'utf-8'
        if response.code == 200:
            data = response.read()
            _value = self.bs4Paraser(data)
            return _value
        else:
            return _value
        
    #resolver html, 传入html格式数据，返回路由器列表
    def bs4Paraser(self, html):
        _allValue = []
        _itemValue = []
        _soup = BeautifulSoup(html, 'html.parser')
        #定位第一个table 标签
        _allRow = _soup.find_all('table',limit=1)
        for _row in _allRow:
            _buf = _row.find_all('tr')
            for _rr in _buf:
                for _routeInfo in _rr.findAll('td'):
                    #获取html row 数据
                    _itemValue.append( _routeInfo.getText().strip())
                if len(_itemValue) == 5:_allValue.append(_itemValue)
                _itemValue = []
        return _allValue
