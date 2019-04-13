#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   MySQL_notes.py
@Time    :   2019/04/13 09:42:55
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
import pymysql

# 链接MySQL数据库 创建新的数据库
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306)  # 端口默认3306
# coursor = db.cursor()  # 获取游标
# coursor.execute('SELECT VERSION()')
# data = coursor.fetchone()
# '''
# def fetchone(self):
# Fetch the next row
# '''

# print("DATAbase version:", data)  # 逗号
# coursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4")
# db.close()

# 链接 MySql 在spiders数据库下创建新的table
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# coursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# coursor.execute(sql)
# db.close()

# 插入数据
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# id = '201828000206058'
# name = 'Lucifer'
# age = 24
# coursor = db.cursor()
# sql = 'INSERT INTO students (id, name, age) values(%s, %s, %s)'  # 格式化符%s 字符串拼接
# try:
#     coursor.execute(sql, (id, name, age))  # 执行语句 与元组值
#     """
#     def execute(query, args=None)
#     Execute a query
#     :param str query: Query to execute.
#     :param args: parameters used with query. (optional) :type args: tuple, list or dict
#     :return: Number of affected rows :rtype: int
#     If args is a list or tuple, %s can be used as a placeholder in the query. If args is a dict, %(name)s can be used as a placeholder in the query.
#     """
#     db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
#     # Commit changes to stable storage.
#     # See Connection.commit() <https://www.python.org/dev/peps/pep-0249/\#commit>_ in the specification.
# except:
#     db.rollback() # 报错执行数据回滚, 相当于什么都没发生
#     # Roll back the current transaction.
#     # See Connection.rollback() <https://www.python.org/dev/peps/pep-0249/\#rollback>_ in the specification.
# db.close()

# 利用字典动态插入数据
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# coursor = db.cursor()
# data = {
#     "id" : '201828000206075',
#     "name" : 'Ferry',
#     "age" : 24
# }
# table = "students"
# keys = ', '.join(data.keys()) # join 链接列表 注意keys要与数据库里面相符
# values = ', '.join(['%s'] * len(data))

# sql = 'INSERT INTO {table} ({keys}) values({values})'.format(table=table, keys=keys, values=values)
# # S.format(*args, **kwargs) -> str  格式化输入
# # Return a formatted version of S, using substitutions from args and kwargs.
# # The substitutions are identified by braces ('{' and '}').
# try:
#     if coursor.execute(sql, tuple(data.values())):  # 执行语句 与元组值
#         print("Successful")
#         db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
#         # Commit changes to stable storage.
#         # See Connection.commit() <https://www.python.org/dev/peps/pep-0249/\#commit>_ in the specification.
# except:
#     print("Failed")
#     db.rollback() # 报错执行数据回滚, 相当于什么都没发生
#     # Roll back the current transaction.
#     # See Connection.rollback() <https://www.python.org/dev/peps/pep-0249/\#rollback>_ in the specification.
# db.close()

#简单的更新数据
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# coursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, "Luceifer"))
#     db.commit()
# except:
#     db.rollback()
# db.close()


# 更新数据 插入数据, 重复则更新
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# coursor = db.cursor()
# data = {
#     "id" : '201828000206075',
#     "name" : 'Ferry',
#     "age" : 22
# }
# table = "students"
# keys = ', '.join(data.keys()) # join 链接列表 注意keys要与数据库里面相符
# values = ', '.join(['%s'] * len(data))

# sql = 'INSERT INTO {table} ({keys}) values({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# # ON DUPLICATE KEY UPDATE 如果主键已经存在就执行更新操作
# update = ', '.join(["{key} = %s".format(key=key) for key in data])  # 列表生成式
# sql += update
# try:
#     if coursor.execute(sql, tuple(data.values())*2):  # 执行语句 与元组值
#         print(tuple(data.values()) * 2)
#         print("Successful")
#         db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
#         # Commit changes to stable storage.
#         # See Connection.commit() <https://www.python.org/dev/peps/pep-0249/\#commit>_ in the specification.
# except:
#     print("Failed")
#     db.rollback() # 报错执行数据回滚, 相当于什么都没发生
#     # Roll back the current transaction.
#     # See Connection.rollback() <https://www.python.org/dev/peps/pep-0249/\#rollback>_ in the specification.
# db.close()

# 删除数据
# db = pymysql.connect(host='localhost', user="root",
#                        password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
# coursor = db.cursor()
# table = 'students'
# condition = 'age > 23'  # 运算符有很多, >, <, =, like等, 条件连接符AND, OR
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     coursor.execute(sql)  # 执行语句 与元组值
#     db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
#     # Commit changes to stable storage.
#     # See Connection.commit() <https://www.python.org/dev/peps/pep-0249/\#commit>_ in the specification.
# except:
#     db.rollback() # 报错执行数据回滚, 相当于什么都没发生
#     # Roll back the current transaction.
#     # See Connection.rollback() <https://www.python.org/dev/peps/pep-0249/\#rollback>_ in the specification.
# db.close()

# 查询数据
db = pymysql.connect(host='localhost', user="root",
                       password="Luozhijun199502@", port=3306, db='spiders')  # 端口默认3306 需要指定数据库
coursor = db.cursor()
table = 'students'
condition = 'age > 20'  # 运算符有很多, >, <, =, like等, 条件连接符AND, OR
sql = 'SELECT * FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    coursor.execute(sql)  # 执行语句 与元组值
    print("Count:", coursor.rowcount)
    one = coursor.fetchone()  # 获取一个 .fetchall()获取所有, fetchmany()获取多个, 
    print(one)
    # 内部有个偏移指针来指向查询结果, 最开始偏移指针指向第一条数据, 取一次以后, 指针偏移到下一个数据, 这样再取就取到下一条数据
    db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
    # Commit changes to stable storage.
    # See Connection.commit() <https://www.python.org/dev/peps/pep-0249/\#commit>_ in the specification.
except:
    db.rollback() # 报错执行数据回滚, 相当于什么都没发生
    # Roll back the current transaction.
    # See Connection.rollback() <https://www.python.org/dev/peps/pep-0249/\#rollback>_ in the specification.
db.close()
