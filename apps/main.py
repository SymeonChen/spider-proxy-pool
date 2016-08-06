#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing.dummy import Pool as ThreadPool

import dboperation
import setting 
import proxyspider
thread_number = setting.thread_number
proxy_list = setting.proxy_web_list


pool = ThreadPool(thread_number)
pool.map(proxyspider.getProxy,proxy_list)
results = dboperation.selectAllAddress()
pool.map(dboperation.checkAllAddress,results)

pool.close()
pool.join() 

