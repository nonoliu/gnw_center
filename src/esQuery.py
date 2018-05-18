#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2017年10月25日

@author: admin
'''
from elasticsearch import Elasticsearch,helpers
import time
from datetime import datetime,timedelta
from src.logMsg import logMessage
from src.config import *
from dataCache import *

LOG = logMessage()

class esQuery(object):
 
#插入数据到ES
    def dataInputES(self):
        try:
            self._es = Elasticsearch(config_es)
            self.cache = dataCache()
            _actions = []
            _currentIndex = "gnw-" + time.strftime("%Y%m%d", time.localtime())
            global pingResultQ
            #读取已经抓取的数据
            while not pingResultQ.empty():
                _items = pingResultQ.get()
                if _items[0]['result'] == 'True':
                    _bufTime = datetime.strptime(_items[0]['timestamp'],'%Y-%m-%d %H:%M')
                    if self.cache.failStat.has_key(_items[0]['address']):
                        self.cache.failStat[_items[0]['address']] = 0
                    for _item in _items[0]['ret']:
                        _bufValue = _item['result'].split(' ')
                        _action = {u'_index':_currentIndex , u'_type':"log", u'_source':{
                        'timestamp':_bufTime,'sourceIP':_item['source'],'desIP':_item['des'],
                        'slng':_items[0]['lng'],'sLat':_items[0]['lat'],'dlng':_item['lng'],'dlat':_item['lat'],
                        'min':_bufValue[0],'avg':_bufValue[1],'max':_bufValue[2]
                        }}
                        _actions.append(_action)
                elif _items[0]['result'] == 'False':
                    if self.cache.failStat.has_key(_items[0]['address']):
                        self.cache.failStat[_items[0]['address']] = self.cache.failStat[_items[0]['address']] +1
                    else:
                        self.cache.failStat[_items[0]['address']] = 1
        except Exception,e :
            LOG.logWirte('error', 'es query:' + str(e), 1)
        
        if len( _actions ) == 0:return "1"
        
        _c = 1
        while True:
            _c = _c + 1
            try:
                helpers.bulk(self._es, _actions, index=_currentIndex, raise_on_error=True)
                break
            except Exception,e:
                if _c > 3 :
                    LOG.logWirte('error', "data input es:" + str(e), 2)
                    break
                time.sleep(1)
        del _actions[0:len(_actions)]
#初始化 index
    def set_mapping(self,es, index_name="content_engine", doc_type_name="log"):
        try:
            my_mapping =  {"mappings":{
                                       "log": {
                    "properties": {
                        "timestamp": {
                            "format": "strict_date_optional_time||epoch_millis",
                            "type": "date"
                        },
                        "sourceIP": {
                            "type": "string"
                        },
                        "desIP": {
                            "type": "string"
                        },
                        "slng": {
                            "type": "string"
                        },
                        "slat": {
                            "type": "string"
                        },
                        "dlng": {
                            "type": "string"
                        },
                        "dlat": {
                            "type": "string"
                        },
                        "min": {
                            "type": "long"
                        },
                        "avg": {
                            "type": "long"
                        },
                        "max": {
                            "type": "long"
                        }
                    }
                        }}}
            
            create_index = es.indices.create(index=index_name,body=my_mapping)
            _WCR = 0
        except Exception,e:
            LOG.logWirte('error', "set mapping:" + str(e), 1)