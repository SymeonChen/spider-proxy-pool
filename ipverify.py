#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import dboperation
import iplocation

def ipverify(address,port,protocol='HTTP'):
    proxy = {'http':"http://"+str(address)+":"+str(port)}
    try:
        response = requests.get("http://httpbin.org/ip",proxies=proxy,timeout = 3).json()["origin"]
        if response==address:
            return True
        return False
    except:
        return False

def deleteAddress(address,port,protocol='HTTP'):
    if(ipverify(address,port,protocol)):
        location = iplocation.getLocation(address)
        dboperation.insert(address=address,port=port,location=location,protocol=protocol)
        # print("success: "+str(address))
    else:
        dboperation.delete(address)
        print("delete: "+str(address))


def checkAllAddress(address):
    port = dboperation.select(address)[0][2]
    deleteAddress(address,port)



# # Use for test!
# address="193.142.213.18"
# port=8080
# print(ipverify(address,port))
