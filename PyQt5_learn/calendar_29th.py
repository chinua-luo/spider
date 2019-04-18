#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   calendar_29th.py
@Time    :   2019/04/18 09:36:49
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This example shows a QCalendarWidget widget
'''
# QCalendarWidget提供了基于月份的日历插件，十分简易而且直观
# QCalendarWidget显示一个日历月份，并允许用户选择日期。
# 日历包括四个组件：一个允许用户更改月份的导航栏,
#               一个每个单元代表每个月每天的网格,
#               两个显示星期名和周数的抬头
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, 
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys
# 这个例子有日期组件和标签组件组成，标签显示被选中的日期
# 信号与槽 https://blog.csdn.net/jia666666/article/details/81774858 或笔记
class Example(QWidget): 
    def __init__(self):
        super().__init__()     
        self.initUI()
               
    def initUI(self):              
        vbox = QVBoxLayout(self)
        # 创建一个横向布局
        cal = QCalendarWidget(self)
        # 创建一个QCalendarWidget
        cal.setGridVisible(True)
        # 设置网格可见
        # 从窗口组件中选定一个日期，会发射一个QCore.QDate信号
        cal.clicked[QDate].connect(self.showDate)  # clicked[QDate]说明点击信号发出,会带有一个QDate参数, 就要求槽函数也要有形参
        # 选择一个日期时, QDate的点击信号就触发了, 
        # 把这个信号和我们自己定义的showDate()方法关联起来
        # 并且传入一个QDate类型的参数(即当前选中的日期)
        vbox.addWidget(cal)
        
        # 自动在底部标签栏显示当前日期的信息
        self.lbl = QLabel(self)
        # 设置日历的最小日期
        # self.cal.setMinimumDate(QDate(1980,1,1))
        # cal.setSelectedDate(QDate(1980,1,1)) 设置选取的日期
        date = cal.selectedDate()
        # 使用selectedDate()方法获取选中的日期, 默认当前日期
        self.lbl.setText(date.toString())
        # 然后把日期对象转成字符串, 在标签栏里面显示出来
        
        vbox.addWidget(self.lbl)
        # 布局中加入标签控件
        self.setLayout(vbox)
        # 设置布局
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
        
        
    def showDate(self, date):      
        self.lbl.setText(date.toString())
        # 然后把日期对象转成字符串, 在标签栏里面显示出来
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())