* [English Version](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README.md)
* [中文版](https://github.com/SymeonChen/spider-proxy-pool/blob/master/README-zh.md)


## 关于
用于从多个代理网站获取代理信息的Python项目。
### 简介
![](/sample-spider.png)

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

### ⚠️注意

本项目仅供学习参考之用，代码中涉及的技术均为网上公开可查的教程所提供，项目中所涉及的第三方站点地址均为通过搜索引擎检索得到的相关站点，仅作为示例之用。本项目多年未更新，不保证其准确性、可靠性、完整性，且不对其衍生项目的任何场景负责。任何使用该项目进行违法用途的行为应当立即停止。

如果您认为该项目的示例网址等信息不利于您的正当权益，欢迎通过邮件向我反馈，我将合理合法配合解决该问题。