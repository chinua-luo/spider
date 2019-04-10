#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   hello.py
@Time    :   2019/04/11 00:45:03
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib

import random
msg = "hello world"
a = random.randint(0, 10)
print(msg)
print(a)
for i in range(0, 10):
    print(i)
print(msg.capitalize()) 