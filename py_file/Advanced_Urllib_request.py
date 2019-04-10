#!/usr/bin/env python3  # 保证可以直接Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-
__Author__: 'Lucifer'
__Date__: "2019/02/26  上午 9:09"
__Name__: 'Advanced_Urllib_request.py'
__IDE__: 'PyCharm'

### cookies处理, 代理设置 ###

"""
urllib.request模块里面的BaseHandler类是其他所有handler类的父类提供了最基本的方法:
    default_open()  protocol_request()

部分子类:
HTTPDefaultErrorHandler: 用于处理HTTP响应错误, 错误都会抛出HTTPError类型的异常
HTTPRedirectHandler: 用于处理重定向
HTTPPasswordMgr: 用于管理密码, 它维护了用户名和密码的表
HTTPBasicAuthHandler: 用于管理认证,如果一个链接打开时需要认证, 就可以用它来解决认证问题
HTTPCookieProcessor: 用于处理Cookies
ProxyHandler: # Proxies must be in front 用于设置代理, 默认代理为空

"""

from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError
"""
    def build_opener(*handlers):
    Create an opener object from a list of handlers.

    The opener will use several default handlers, including support
    for HTTP, FTP and when applicable HTTPS.

    If any of the handlers passed as arguments are subclasses of the
    default handlers, the default handlers will not be used.
"""
# 弹出式验证
username = '980532773@qq.com'
password = '34122619940119231X'
URL = 'http://sep.ucas.ac.cn/'  #

p = HTTPPasswordMgrWithDefaultRealm()  # 一个类实例
p.add_password(None, URL, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(URL)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

# 更多见崔庆才的python3网络爬虫开发实践

