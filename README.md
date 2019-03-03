* [English Version](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README.md)
* [中文版](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README-zh.md)

## About

A python program to get lists of proxy information from proxy websites.
### Introduction
![](https://blog-1252276648.cos.ap-shanghai.myqcloud.com/spider.png)

It will create a sqlite database for proxy information including ip address, port, location and protocol.
### Usage
Python version must greater than 3.3

Clone the code.

``` shell
git clone https://github.com/SymeonChen/spider-proxy-pool.git
```

Install dependency.
```shell
sh install.sh
```

run the apps.
```shell
sh run.sh
```

Now we can get http proxy lists from
```shell
http://localhost:5000/api/http
```
