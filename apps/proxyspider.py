#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

import dboperation
import setting
from tools import iptools as iptools
from tools import headertools as headertools

proxy_web_list = setting.proxy_web_list
proxy_web_loop_number = setting.proxy_web_loop_number

def getProxy(website,maxrange = proxy_web_loop_number,isproxy = False):

    if(isproxy):
        #TODO
        pass
    else:
        proxy = None
    for n in range(1,maxrange):
        
        ip_website = website+str(n)
        print("Scanning website: "+ip_website)

        header_info = headertools.getHeaderOfPC(proxy_web_list)

        response = requests.get(ip_website,headers = header_info,proxies = proxy)

        soup = BeautifulSoup(response.text,'lxml')

        result = soup.find_all('td')

        for i,e in enumerate(result,0):

            temp = e.text
            # print(temp)

            if iptools.ip_isvalid(temp):
                address=temp
            elif iptools.port_isvalid(temp):
                port = temp
            elif iptools.protocol_isvalid(temp):
                protocol = temp
                print(address,port,protocol)
                dboperation.insert(address=address,port=port,location="",protocol=protocol)

