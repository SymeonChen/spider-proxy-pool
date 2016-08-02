#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing.dummy import Pool as ThreadPool
import proxyspider
import dboperation
import ipverify

proxy_list = [
"http://www.kuaidaili.com/free/inha/",
"http://www.kuaidaili.com/free/outha/",
"http://ip84.com/dlgn/",
"http://ip84.com/gwgn/",
"http://www.xicidaili.com/wn/",
"http://www.xicidaili.com/nn/",
"http://www.ip3366.net/free/?stype=1&page=",
"http://www.ip3366.net/free/?stype=3&page=",
"http://www.mimiip.com/gngao/",
"http://www.mimiip.com/hw/"
]

pool = ThreadPool(30)

pool.map(proxyspider.getProxy,proxy_list)

results = dboperation.selectAllAddress()
pool.map(ipverify.checkAllAddress,results)

pool.close()
pool.join() 

