#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   xpath_note.py
@Time    :   2019/04/12 18:14:16
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
from lxml import etree

'''
@           选取属性
..          选取当前节点的父节点
.           选取当前节点
//          从当前节点选取子孙节点
/           从当前节点选取直接子节点

exm: //title[@lang='eng'] 代表选取所有名称为title, 属性lang的值为'eng'的节点
'''
html = etree.parse('./downloads/text.html', etree.HTMLParser(encoding='utf8')) # 注意编码
# res = html.xpath("//*")  #  * 代表匹配所有节点 i.e. HTML文本中所有节点都会被捕获, 返回一个列表
# print(res) # 每个元素都是Element类型

# res = html.xpath("//a")  #  li 代表匹配所有li节点 , 返回一个列表
# print(res)
# print(res[0])

# / 子节点 ,   // 子孙节点
# res = html.xpath("//div/a")  # 所有div的所有直接a子节点, //div//a选取所有div节点的所有子孙节点
# print(res)
# print(res[0])

# res = html.xpath('//a[@href="http://www.runoob.com/ado"]/../@class')
# #  选取所有href属性为"http://www.runoob.com/ado"的a节点, 然后再获取其父节点,再获取其class属性值
# print(res)
# 也可以如下, parent::*获取父节点
# res = html.xpath('//a[@href="http://www.runoob.com/ado"]/parent::*/@class')
# #  选取所有href属性为"http://www.runoob.com/ado"的a节点, 然后再获取其父节点,再获取其class属性值
# print(res)

# 属性匹配 @进行属性过滤
# res = html.xpath('//a[@href="http://www.runoob.com/ado"]')
# # 选取所有href属性为"http://www.runoob.com/ado"的a节点
# print(res)  # Element类型

# res = html.xpath('//a[@href="http://www.runoob.com/ado"]/text()')
# # 选取所有href属性为"http://www.runoob.com/ado"的a节点 
# # / 的直接子节点文本, 子节点内部的文本不会被匹配到, 匹配到的是a节点的内部文本
# print(res[0])  # 文本 列表形式


# res = html.xpath('//a[@href="http://www.runoob.com/ajax"]/@title')
# # 选取所有href属性为"http://www.runoob.com/ado"的a节点的title属性
# print(type(res[0]))  # 列表形式 值  <class 'lxml.etree._ElementUnicodeResult'>
# print(str(res[0]))

# res = html.xpath('//a[@href="http://www.runoob.com/ado"]/text()')
# # 选取所有href属性为"http://www.runoob.com/ado"的a节点的title属性
# print(type(res[0]))  # 列表形式 值  <class 'lxml.etree._ElementUnicodeResult'>
# print(str(res[0]))


# 属性多值匹配
# res = html.xpath('//a[contains(@href, "http://www.runoob.com/ado")]')
# # 选取所有href属性为"http://www.runoob.com/ado"的a节点的title属性
# print(type(res))  

# 多属性匹配
# res = html.xpath('//a[contains(@href, "http://www.runoob.com/ado") and @title="西瓜hhhh"]')

# res = html.xpath('//a[last()]')  # 所有匹配的a节点里面最后一个
# res = html.xpath('//a[1]') # 所有匹配的a节点里面第一个 从 1 开始计数
# res = html.xpath('//a[position()<3]')  # 所有匹配的a节点里面位置小于3的节点, 即1, 2
# res = html.xpath('//a[last()-2]') # 所有匹配的a节点里面倒数第三个

# 节点轴选择
res = html.xpath('//a[last()]/ancestor::*')  # 调用ancestor轴其后跟::, *匹配所有节点
# print(res)
res = html.xpath('//a[last()]/ancestor::div')  # 调用ancestor轴其后跟::, 匹配div节点
res = html.xpath('//a[last()]/attribute::*')  # 调用attribute轴其后跟::, *获取所有属性 可以加限定条件
res = html.xpath('//a[last()]/child::*')  # 调用child轴其后跟::, *匹配所有直接子节点 可以加限定条件
res = html.xpath('//a[last()]/descendant::*')  # 调用descendant轴其后跟::, *匹配所有子孙节点, 可以加限定条件
res = html.xpath('//a[last()]/following::*[2]')  # 调用following轴其后跟::, *匹配当前节点之后的节点, [2]第二个后续节点
res = html.xpath('//a[last()]/following-sibling::*')  # 调用following轴其后跟::, *匹配当前节点之后的所有同级节点







