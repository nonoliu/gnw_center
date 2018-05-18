#!/usr/bin/env python
#coding:utf-8
'''
Created on 2012-11-5

@author: Administrator
'''
#Python的线程池实现
import sys
import Queue
import threading

class proInfo:
    def __init__(self):
        self._indexStatus = ['',200]
        self._fileSeek = 0
        self._WCR = 0

#替我们工作的线程池中的线程
class MyThread(threading.Thread):
    def __init__(self, workQueue, resultQueue, resinfo=1, timeout=120,**kwargs):
        threading.Thread.__init__(self)
        #线程在结束前等待任务队列多长时间
        self.timeout = timeout
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.start()
        self.resinfo = resinfo
 
    def run(self):
        while True:
            try:
                #从工作队列中获取一个任务
                callable, args = self.workQueue.get(timeout=self.timeout)
                #我们要执行的任务
                #res = callable(args)
                if self.resinfo == 0:
                    res = callable(args)
                #报任务返回的结果放在结果队列中
                    self.resultQueue.put(res)
                else :
                    callable(args)
                    
            except Queue.Empty: #任务队列空的时候结束此线程
                break
            except :
                print sys.exc_info()
                raise
     
class ThreadPool:
    def __init__( self, num_of_threads=1000, resinfo = 1):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.threads = []
        self.resinfo = resinfo
        self.__createThreadPool( num_of_threads )

    def __createThreadPool( self, num_of_threads ):
        for i in range( num_of_threads ):
            thread = MyThread( self.workQueue, self.resultQueue, self.resinfo )
            self.threads.append(thread)

    def wait_for_complete(self):
        #等待所有线程完成。
        while len(self.threads):
            thread = self.threads.pop()
            #等待线程结束
            if thread.isAlive():#判断线程是否还存活来决定是否调用join
                thread.join()
    
    def add_job( self, callable, *args):
        try:
            self.workQueue.put( (callable,args) )
        except Exception as e:
            print e