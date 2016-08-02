#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

import proxyisvalid
import dboperation
import headerall

def getProxy(website,maxrange = 3,isproxy = False):

    if(isproxy):
        #TODO
        pass
    else:
        proxy = None
    for n in range(1,maxrange):
        
        ip_website = website+str(n)
        print("Scanning website: "+ip_website)

        header_info = headerall.getHeader()

        response = requests.get(ip_website,headers = header_info,proxies = proxy)

        soup = BeautifulSoup(response.text,'lxml')

        result = soup.find_all('td')

        for i,e in enumerate(result,0):

            temp = e.text

            if proxyisvalid.ip_isvalid(temp):
                address=temp
            elif proxyisvalid.port_isvalid(temp):
                port = temp
            elif proxyisvalid.protocol_isvalid(temp):
                protocol = temp
                dboperation.insert(address=address,port=port,location="",protocol=protocol)

