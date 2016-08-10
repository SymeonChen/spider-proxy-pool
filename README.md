* [English version](#about)

* [中文版](#关于)

## About

A python program to get lists of proxy information from proxy websites.
### Introduction
![](http://oa5cno1tg.bkt.clouddn.com//web/image/20160802/spider.png)

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



## 关于
用于从多个代理网站获取代理信息的Python项目。
### 简介
![](http://oa5cno1tg.bkt.clouddn.com//web/image/20160802/spider.png)

运行后会创建一个sqlite数据库，包含IP地址，端口号，位置，协议。
### 使用方法
Python版本需大于3.3

clone项目到本地

``` shell
git clone https://github.com/SymeonChen/spider-proxy-pool.git
```

安装依赖模块
```shell
sh install.sh
```

运行项目
```shell
sh run.sh
```
运行完毕后即可通过
```shell
http://localhost:5000/api/http
```
来获取http代理列表。
