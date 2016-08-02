#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import proxyisvalid

def getLocation(address):
    try:
        if(proxyisvalid.ip_isvalid(address)):
            par = {'ip': address}
            response = requests.get('http://ip.taobao.com/service/getIpInfo.php',params = par)
            re_json = response.json()
            region = re_json['data']['country'][:2]
            if(region=='中国'):
                return '墙内'
            return region
        else:
            return ''
    except Exception as e:
        print(str(e))
        return ''
