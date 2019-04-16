#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   Parser_Ajax.py
@Time    :   2019/04/13 22:23:11
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib


# 瀑布流网页的爬取方案
# Ajax请求到网页更新分三步
# 1. 发送请求
# 2. 解析内容
# 3. 渲染页面

# 用chrome打开网页(下拉更新式的)
# 右击 inspect(ctrl+shift+i) 在Element选项卡可以看到源码
# 切换到Network选项卡, 刷新页面检查多出了什么条目
# Ajax为特殊的请求类型, xhr类型, 右击这个类型的条目,查看请求的详细内容
# 以https://search.jd.com/Search?keyword=gxg%E7%94%B7%E5%A3%AB&enc=utf-8&suggest=
# 1.def.0.V07--featuredump,&wq=gxg&pvid=b3d0030ff40242c788e0781832aea302 为例
# 可以看到 URL, Request Headers和Response Headers 信息
# 其中Request Headers有一个信息为 X-Requested-With: XMLHttpRequest ,这就标记了此请求为Ajax请求
# 点击preview可以看到响应的内容, 为json格式
# 原始第一个请求response选项卡,可以看到真实的返回数据, 即这个网页最初html代码
# 通过滑动页面更新加载, 可以看到一条条Ajax条目被加载出来
# 仔细观察其Request Url,Request Headers, Response Headers,  Response Body 等内容就可以模拟请求了

# python模拟Ajax请求, 查看其变化规律
# GET请求, 
# 请求链接 https://search.jd.com/im.php?r=1909846668&t=1555166044.7166&cs=f9e0bdfab3ec39016933c55953f15de9
# 下面有个Query String Parameter 列出了一些关键参数, view encode, 则会有对应的编码字符
# 查看此京东页面时发现, 每页60条信息, 分两次加载,前三十直接打开, 后三十动态打开, 会有如下xhr条目会加载出来
# https://search.jd.com/s_new.php?keyword=gxg%E7%94%B7%E5%A3%AB&enc=utf-8&qrst=1&rt=1&stop=1&
# vt=2&suggest=1.def.0.V07--featuredump%2C&wq=gxg&page=2&s=27&scrolling=y&log_id=1555166044.13020&
# tpl=3_L&show_items=42334415313,17754147707,29880299181,37782144724,42334406252,32525071297,32525470624,
# 40654161342,34460344720,42334447286,32525083313,31644663656,32794438177,32215932995,32422560956,16778916096,
# 32901391039,32525063944,42334443688,44583805715,32603732280,32469407518,41241737999,32469567562,44328519042,
# 32469390378,43689013219,37779682039,44270163318,32525254906
# 至于后30条信息的url的变化规律，我们先看下这个网址，很长。首先url尾部的一串数字共30个，很容易想到是当页前30条商品的ID，实际发送请求时去掉也不影响。还有tpl=3也可以去掉，不影响。
# 变成如下
# https://search.jd.com/s_new.php?keyword=gxg%E7%94%B7%E5%A3%AB&enc=utf-8&qrst=1&rt=1&stop=1&
# vt=2&suggest=1.def.0.V07--featuredump%2C&wq=gxg&page=2&s=27&scrolling=y&log_id=1555166044.13020
# url包含三个变化的参数,page,s还有log_id, log_id这个参数其实就是Unix时间戳，表示当前的时间，直接调用time函数就可以得到
# page就是当前页数 n*2 