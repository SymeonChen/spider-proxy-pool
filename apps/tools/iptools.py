#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ipaddress
# To use ipaddress module, the version of Python must be greater than 3.3

import requests


def ip_isvalid(address):
    try: 
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

def port_isvalid(port):
    try:    
        if( int(port) < 65535 and int(port) > 1):
            return True
        else:
            return False
    except ValueError:
        return False

def protocol_isvalid(protocol=""):
    try:
        if(protocol.upper()=="HTTP" or protocol.upper()=="HTTPS"):
            return True
        else:
            return False
    except AttributeError as e:
        print("Parameter must be string. "+str(e))
        return False

def getLocation(address):
    try:
        if(ip_isvalid(address)):
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

def ipverify(address,port,protocol='HTTP'):
    proxy = {'http':"http://"+str(address)+":"+str(port)}
    try:
        response = requests.get("http://httpbin.org/ip",proxies=proxy,timeout = 3).json()["origin"]
        if response==address:
            return True
        return False
    except:
        return False


# # Use for test!
# address="193.142.213.18"
# port=8080
# print(ipverify(address,port))



