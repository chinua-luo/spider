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
import re

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
# print(soup.a.next_sibling) # 有可能是空格
# print(list(enumerate(soup.a.next_siblings))[1])

# 方法选择器
# soup.find_all()
'''
def find_all(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
API
Extracts a list of Tag objects that match the given
criteria.  You can specify the name of the Tag and any
attributes you want the Tag to have.

The value of a key-value pair in the 'attrs' map can be a
string, a list of strings, a regular expression object, or a
callable that takes a string and returns whether or not the
string matches for some custom definition of 'matches'. The
same is true of the tag name."""
'''
# print(soup.find_all(name = 'a'))
# print(type(soup.find_all(name = 'a')[0]))  # <class 'bs4.element.Tag'> 标签类型 可以嵌套

# print(soup.find_all(attrs = {'title': '西瓜hhhh'}))  # 返回列表, 每一个均为标签类型
# print(soup.find_all(class_ = 'sdsd'))  # 也可以这样查询属性class值为sdsd的标签(class_是由于class是python内置关键词)

# text 匹配节点内容
# print(soup.find_all(text = re.compile('D')))
# 返回所有匹配正则表达式的节点文本内容

# find 返回第一个匹配到的元素 API相同
# soup.find_all_next()
# soup.find_next()
# soup.find_next_sibling()
# soup.find_next_siblings()

# soup.find_parent()
# soup.find_parents()

# soup.find_previous()
# soup.find_all_previous()
# soup.find_previous_sibling()
# soup.find_previous_siblings()

# css选择器
# print(soup.select('div a')) # 所有div下所有a节点
# print(type(soup.select('div a')[1])) # <class 'bs4.element.Tag'> 标签类型 可以嵌套

# 每个节点类型仍是Tag类型 仍可以 a['title'] 或 a.attrs['title'] 获取属性

# 获取文本 二者一样获取文本
for i in soup.select('a'):
    print(i.get_text())
    print(i.string)


