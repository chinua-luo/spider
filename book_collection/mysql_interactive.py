#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   mysql_interactive.py
@Time    :   2019/04/15 20:59:54
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
import books_collection_setting as bcs




class interactive(object):
    def __init__(self, db):
        self.db = db
        self.coursor = self.db.cursor()
        self.insert_sql = bcs.INSERT_SQL
        self.delete_sql = bcs.DELETE_SQL
        self.select_sql = bcs.SELECT_SQL
        self.select_sql_all = bcs.SELECT_SQL_ALL
        self.data = bcs.DATA
    
    # 插入, 若 name 与 author 相同则覆盖
    def insert(self):
        try:
            if self.coursor.execute(self.insert_sql, tuple(self.data.values())*2):  # 执行语句 与元组值
                print("Successful")
                self.db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
        except Exception as e:
            print(e)
            print("Failed")
            self.db.rollback()  # 报错执行数据回滚, 相当于什么都没发生

    # 删除 删除严格符合条件的条目    
    def delete(self, condition):
        if condition:  # 判断condition为真是, 即非空执行以下语句
            self.delete_sql += condition
            print(self.delete_sql)
            try:
                if self.coursor.execute(self.delete_sql):  # 执行语句 与元组值
                    print("Successful")
                    self.db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
            except Exception as e:
                print(e)
                print("Failed")
                self.db.rollback()  # 报错执行数据回滚, 相当于什么都没发生
    
    # 列出所有符合条件的条目, 若信息不全, 可仅是别给出的字段
    def select(self, condition):
        if condition and condition != ' ':  # 判断condition为真是, 即非空执行以下语句 收索用like语句
            print(condition)
            self.select_sql += condition
            print(self.select_sql)
            try:
                if self.coursor.execute(self.select_sql):  # 执行语句 与元组值
                    print("Successful")
                    print(self.coursor.rowcount)
                    row = self.coursor.fetchone()
                    while row:
                        print(row)
                        row = self.coursor.fetchone()
                    self.db.commit()  # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
            except Exception as e:
                print(e)
                print("Failed")
                self.db.rollback()  # 报错执行数据回滚, 相当于什么都没发生
        else:  # 没有条件则查询所有
            try:
                if self.coursor.execute(self.select_sql_all):  # 执行语句 与元组值
                    print("Successful")
                    print(self.coursor.rowcount)
                    row = self.coursor.fetchone()
                    while row:
                        print(row)
                        row = self.coursor.fetchone()
                    self.db.commit()   # 这个语句才是真正将语句提交到数据库执行的方法, 对于数据的插入更新,删除,都需要调用该方法
            except Exception as e:
                print(e)
                print("Failed")
                self.db.rollback()  # 报错执行数据回滚, 相当于什么都没发生


if __name__ == "__main__":
    db = bcs.pymysql.connect(host='localhost', user="root",
                       password="Luozhijun199502@", port=3306, db="books")  # 端口默认3306 需要指定数据库
    coursor = db.cursor()  # 获取游标
    my = interactive(db)
    my.insert()
    db.close()