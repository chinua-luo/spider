#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   books_collection_setting.py
@Time    :   2019/04/15 20:57:24
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
import pymysql
from PyQt5.QtCore import QThread, QSize
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os

TABLE = "physical_books"
DATA = {
    "name" : '*',
    "authors" : '*',
    "list": '*',
    "short_desc": ' '
}



# 和table条目保持一致
VALUES = ', '.join(['%s'] * len(DATA))
KEYS = ', '.join(DATA.keys()) # join 链接列表 注意keys要与数据库里面相符
insert_sql = 'INSERT INTO {table} ({keys}) values ({values})  ON DUPLICATE KEY UPDATE '.format(table=TABLE, keys=KEYS, values=VALUES)
update = ', '.join(["{key} = %s".format(key=key) for key in DATA])
DELETE_SQL = 'DELETE FROM {table} WHERE '.format(table=TABLE)
SELECT_SQL = 'SELECT * FROM {table} WHERE '.format(table=TABLE)
SELECT_SQL_ALL = 'SELECT * FROM {table} '.format(table=TABLE)
INSERT_SQL = insert_sql + update
# DATA = {
#     "name" : '黎曼几何引论(下)',
#     "author" : '陈维桓, 李兴霄',
#     "list": '北大数学系列丛书',
#     "short_desc": ' '
# }
if __name__ == "__main__":
    print(INSERT_SQL)
