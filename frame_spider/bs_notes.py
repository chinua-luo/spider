#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   bs_notes.py
@Time    :   2019/04/12 23:37:45
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
from bs4 import BeautifulSoup

html = open('./downloads/text.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'lxml')  # 初始化时候, 对不标准的 html 自动更正格式
# print(soup.prettify())  # 这个方法可以把要解析的字符串以标准的缩进格式输出
# print(soup.title.string)  # 输出 html 中 title 节点的文本内容
# print(soup.head) # 输出整个 head 部分
# print(soup.a) # 输出第一个 a 节点

# 提取信息
print(soup.a.name) # 输出节点名称 a 

# 获取属性
# print(soup.a.attrs)  # 输出节点a的所有属性与值 键值对 字典print(soup.a.attrs[title]) 获取属性 title 值
# print(soup.a['title'])  # 获取属性 title 值

# 获取内容
# print(soup.a.string) # 获取节点内容

# 嵌套选择
# variable = soup.head.title
# print(variable)
# print(type(variable))
# print(variable.string)

# 子节点 与子孙节点
# print(soup.div.contents)  # 返回为列表, div的直接子节点与文本
# print(len(soup.div.contents))

# print(soup.div.children) # 直接子节点
# 返回一个 列表生成器 <list_iterator object at 0x0000015E6B998128>

# print(soup.div.descendants) # 返回所有子孙节点生成器
# <generator object descendants at 0x000001533D31D5C8>

# print(soup.a.parent) # 父节点的所有内容
# print(type(soup.a.parents)) # <class 'generator'>
# print(list(enumerate(soup.a.parents))) # 所有祖先形成列表
'''
enumerate(iterable[, start]) -> iterator(迭代器) for index, value of iterable
Return an enumerate object. iterable must be another object that supports iteration. 
The enumerate object yields pairs containing a count (from start, which defaults to zero) 
and a value yielded by the iterable argument. enumerate is useful for obtaining an indexed list:
'''
# sf = soup.a
# 兄弟节点
# print(sf.next_sibling)  # 后一节点
# print(soup.a.previous_sibling)  # 前一节点
# print(list(enumerate(a.next_siblings)))
# print(list(enumerate(a.previous_siblings))) 


# 提取信息
print(soup.a.next_sibling) # 有可能是空格
print(list(enumerate(soup.a.next_siblings))[1])