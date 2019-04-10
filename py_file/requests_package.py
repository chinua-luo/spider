#!/usr/bin/env python3  # 保证可以直接Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-
__Author__: 'Lucifer'
__Date__: "2019/02/26  下午 7:31"
__Name__: 'requests_package.py'
__IDE__: 'PyCharm'

# import requests

# 更方面的处理Cookies, 登录验证,代理设置
# URL = 'https://httpbin.org/get'
# r = requests.get(URL)
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# def get(url, params=None, **kwargs):
"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
"""

#  抓取网页
# import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
# URL = 'http://www.zhihu.com/explore'
# r = requests.get(URL, headers=headers)
# # 抓取标题
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, r.text)
# for news in title:
#     print(news.strip())


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
# URL = 'http://www.zhihu.com/explore'
# r = requests.get(URL, headers=headers)
# # 抓取图片
# pattern = re.compile('zh-summary summary clearfix.*?<img .*?\"(.*?)\" data-caption', re.S)
# title = re.findall(pattern, r.text)
# for news in title:
#     img = requests.get(news)
#     res = news.split('/')[-1]
#     with open(res, 'wb') as f:
#         f.write(img.content)


################高级用法######################

# 利用cookie进入登陆状态
# import requests
# headers = {
#     'Cookie': 'l_n_c=1; q_c1=66c76c3479654aaf926a8b10fc284c9c|1551183211000|1551183211000; _xsrf=3ab6fc345f58dc34f83249cb3f0b8b55; r_cap_id="MzQzMGViNDM2MTY2NDZjMTg3MmYxY2JiM2Q4OGJmY2E=|1551183211|3a18604f318dc035fbed19ca01510fe84da209f2"; cap_id="N2MxMDE4N2I1NTRmNDlmZDkzOGFkNmM2ZWJkOGI2OWE=|1551183211|8e1d46d9c9a2eadea481e61b553ebc885feb5140"; l_cap_id="ZGIyYmJmYmEzODk4NDFiZWExNjNiNWQwZTA5N2NiM2Q=|1551183211|8d9e3623b1fafae79e54772345b3f5718692a35f"; n_c=1; d_c0="AKCkBwmCCg-PThuwVVxoAlbb65tzFyPv-d8=|1551183214"; __utmc=51854390; __utmz=51854390.1551183214.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _zap=ff50df0c-8906-4f6a-bb7d-a8f74322b910; _xsrf=iync0udXWYY3jlzj6yjhxJ5dPlgczMOP; __utma=51854390.2031615734.1551183214.1551183214.1551183252.2; __utmb=51854390.0.10.1551183252; tgw_l7_route=025a67177706b199591bd562de56e55b; tst=r; __utmv=51854390.100-1|2=registration_date=20150317=1^3=entry_date=20150317=1; capsion_ticket="2|1:0|10:1551189286|14:capsion_ticket|44:OGFiYTk5Y2FlMmViNGIxNWIyNjFlMTM0M2NkMTM2YjU=|cf82edb7463b7ed13ae7beb00798a0cc41ffae18b20888fee99b1af2ffdb9ce0"; z_c0="2|1:0|10:1551189307|4:z_c0|92:Mi4xQkVVTEFRQUFBQUFBb0tRSENZSUtEeVlBQUFCZ0FsVk5PcE5pWFFEZWlHcnk0a3B5VzE2Vl9vbjhGOXNIeDhLZC1n|89da7a99953d3de486f538e97bd0ef3c869837c34cbd516a2e749c33c92a941a"',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
#
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)


# 代理设置
# import requests.exceptions
# proxies = {
#     # 'http': 'http://180.118.242.134:9999',
#     'http': 'http://118.190.95.35:9001'
# }
# URL = 'http://httpbin.org/ip'
# try:
#     res = requests.get(URL, proxies=proxies)
#     print(res.text)
# except requests.exceptions.ProxyError:
#     print('代理无效')
# 没有proxies时
"""
输出
{
  "origin": "111.207.250.54, 111.207.250.54"
}
或者
代理无效
ConnectionRefusedError
urllib3.exceptions.NewConnectionError
urllib3.exceptions.MaxRetryError
requests.exceptions.ProxyError

有可用的代理时输出
{
  "origin": "118.190.95.35, 118.190.95.35"
}
"""

# import requests.adapters
# IPAgents = [
#     "47.96.148.248:8118",
#     "118.190.95.35:9001"  # 只有这个有效目前
#     "180.118.242.134:9999"
#     "60.167.23.213:27339"
# 	]
# URL = "http://icanhazip.com/"
# try:
#     requests.adapters.DEFAULT_RETRIES = 3
#     IP = IPAgents[3]
#     thisProxy1 = "http://" + IP
#     thisIP = "".join(IP.split(":")[0:1])
#     proxies = {"http": thisProxy1}
#     res = requests.get(URL, timeout=8, proxies=proxies)
#     proxyIP = res.text
#     print(proxyIP)
#     print(thisIP)
# except:
#     print("代理IP无效！")


# 超时设置
import requests

r = requests.get('https://www.taobao.com', timeout= 1)

# get的参数和request参数一样
# def request(method, url, **kwargs):
"""
    Constructs and sends a :class:`Request <Request>`.
    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the body of the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      <Response [200]>
"""











