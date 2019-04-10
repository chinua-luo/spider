#!/usr/bin/env python3  # 保证可以直接Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-
__Author__: 'Lucifer'
__Date__: "2019/02/25  下午 11:25"
__Name__: 'urllib_request.py'
__IDE__: 'PyCharm'


# import urllib.request

# URL = 'https://www.python.org'
# response = urllib.request.urlopen(URL)
# print(response.read().decode('utf-8'))
# print(response.status)  # 响应的状态码
# print(response.getheaders())  # 响应的头信息
# print(response.getheader("Server"))  # 获取头信息中Server的值  值为nginx(说明服务器是用nginx搭建)


"""
    urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None):
    Open the URL url, which can be either a string or a Request object.

    *data* must be an object specifying additional data to be sent to
    the server, or None if no such data is needed.  See Request for
    details.

    urllib.request module uses HTTP/1.1 and includes a "Connection:close"
    header in its HTTP requests.

    The optional *timeout* parameter specifies a timeout in seconds for
    blocking operations like the connection attempt (if not specified, the
    global default timeout setting will be used). This only works for HTTP,
    HTTPS and FTP connections.

    If *context* is specified, it must be a ssl.SSLContext instance describing
    the various SSL options. See HTTPSConnection for more details.

    The optional *cafile* and *capath* parameters specify a set of trusted CA
    certificates for HTTPS requests. cafile should point to a single file
    containing a bundle of CA certificates, whereas capath should point to a
    directory of hashed certificate files. More information can be found in
    ssl.SSLContext.load_verify_locations().

    The *cadefault* parameter is ignored.

    This function always returns an object which can work as a context
    manager and has methods such as

    * geturl() - return the URL of the resource retrieved, commonly used to
      determine if a redirect was followed

    * info() - return the meta-information of the page, such as headers, in the
      form of an email.message_from_string() instance (see Quick Reference to
      HTTP Headers)

    * getcode() - return the HTTP status code of the response.  Raises URLError
      on errors.

    For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse
    object slightly modified. In addition to the three new methods above, the
    msg attribute contains the same information as the reason attribute ---
    the reason phrase returned by the server --- instead of the response
    headers as it is specified in the documentation for HTTPResponse.

    For FTP, file, and data URLs and requests explicitly handled by legacy
    URLopener and FancyURLopener classes, this function returns a
    urllib.response.addinfourl object.

    Note that None may be returned if no handler handles the request (though
    the default installed global OpenerDirector uses UnknownHandler to ensure
    this never happens).

    In addition, if proxy settings are detected (for example, when a *_proxy
    environment variable like http_proxy is set), ProxyHandler is default
    installed and makes sure the requests are handled through the proxy.

"""

""" 测试一下data传入 """
# import urllib.parse
# import urllib.request
# URL = 'http://httpbin.org/post'
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen(URL, data=data)
# # data传入必须 bytes(字节流)类型. 如果是字典,可以先用urllib.parse模块里的urlencode()编码
# print(response.read())

"""
answer:
b'{
    "args": {}, 
    "data": "", 
    "files": {}, 
    "form": {
        "word": "hello"
        }, 
    "headers": {
        "Accept-Encoding": "identity", 
        "Content-Length": "10", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "Python-urllib/3.6"     # 默认User-Agent
        }, 
    "json": null, 
    "origin": "111.207.250.54, 111.207.250.54", 
    "url": "https://httpbin.org/post"
    }'

"""

""" 测试一下timeout设置 """
# import socket
# import urllib.error
# URL = 'http://httpbin.org/get'
#
# try:
#     response = urllib.request.urlopen(URL, timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):  # e.reason 表明异常的原由, 即异常类型
#         print("TIME OUT")


from urllib import request, parse

URL = 'http://httpbin.org/post'

header = {
    "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "Host": 'httpbin.org'
}
dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=URL, data=data, headers=header, method='POST')

# req = request.Request(url=URL, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

response = request.urlopen(req)
print(response.read().decode('utf-8'))

"""
class Request:
def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
1. 第一个url必传参数, 其他参数可选
2. data传入必须 bytes(字节流)类型. 如果是字典,可以先用urllib.parse模块里的urlencode()编码                 
3. 第三个参数headers是一个字典, 它就是请求头,可以在构造请求时通过headers参数直接构造
    也可以通过调用请求实例的add_header()方法添加
    
    添加请求头最常用的方法就是通过修改User-Agent来伪装浏览器, 默认的User-Agent是Python-urllib/3.6, 我们可以
    通过修改它来伪装浏览器. 比如要伪装火狐浏览器就可以设置为:
    Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
4. origin_req_host指的是请求方的host名称或IP地址
5. unverifiable表示这个请求是否是无法验证的,默认是False, 意思就是说用户没有足够权限来选择接受这个请求的结果.
    例如我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，我们就要将unverifiable的值设置成True
6. method 参数指的是发起的 HTTP 请求的方式，有 GET、POST、DELETE、PUT等
"""


