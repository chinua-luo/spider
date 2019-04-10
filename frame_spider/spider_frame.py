# 爬虫代码框架
# 爬虫调度器 URL管理器 HTML下载器 HTML解析器　数据储存器
# 各个作用部件的作用

# 爬虫调度器: 主要配合调用其它四个模块,所谓调度就是去调用其它模块

# URL管理器:就是负责管理URL链接的,URL链接分为已经爬取的和未爬取的,这就需要URL管理器来管理它们
# 同时他也为获取新URL链接提供接口

# HTML下载器:就是将要爬取的页面的HTML下载下来

# HTML解析器:就是将要爬取的数据从HTML源码中获取出来,同时也将新的URL链接发送给URL管理器以及将处理后的数据发送给数据处理器

# 数据处理器:就是将HTML下载器发送过来的数据储存到本地

import requests

# URLManager.py

class URLManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def new_url_size(self):
        # 获取未爬取的url大小
        return len(self.new_urls)
    
    def old_url_size(self):
        #获取已爬去的url大小
        return len(self.old_urls)

    def has_new_urls(self):
        # 判断是否有未爬取的url
        return self.new_url_size() != 0
    
    def get_new_url(self):
        # 获取一个为获取的链接
        new_urls = self.new_urls.pop()
        # 获取之后, 将其添加到已爬取的链接
        self.old_urls.add(new_urls)

        return new_urls
    
    def add_new_url(self, url):
        # 将新连接添加到未爬取的集合中(单个链接)

        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    def add_new_urls(self, urls):
        # 将新连接添加到未爬取的集合中(集合)
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    

# HTML下载器
#HTMLDownload.py

class HTMLDownload(object):
    def download(self, url):
        if url is None:
            return
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        res = s.get(url)
        # 判断是否正常获取

        if res.status_code == 200:
            res.encoding = "utf-8"
            res = res.text
            return res
        return None
