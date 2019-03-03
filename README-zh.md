* [English Version](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README.md)
* [中文版](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README-zh.md)


## 关于
用于从多个代理网站获取代理信息的Python项目。
### 简介
![](https://blog-1252276648.cos.ap-shanghai.myqcloud.com/spider.png)

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
