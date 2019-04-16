#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   seventh_statusbar.py
@Time    :   2019/04/16 10:29:54
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program creates a statusbar.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
# 状态栏是由QMainWindow创建的

class Example(QMainWindow): 
    def __init__(self):
        super().__init__()
        # 初始化
        self.initUI()
        
        
    def initUI(self):               
        self.statusBar().showMessage('Ready')
        # 调用QMainWindow类的statusBar()方法，创建状态栏。
        # 第一次调用创建一个状态栏，返回一个状态栏对象。showMessage()方法在状态栏上显示一条信息。
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())