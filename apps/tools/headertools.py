#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

def getHeaderOfPC(header_pc):
    random_header = random.sample(header_pc, 1)
    header = dict(('User-Agent', value) for value in random_header)
    return header
    #output example
    #{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'}