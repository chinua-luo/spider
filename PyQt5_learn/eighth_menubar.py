#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   eighth_menubar.py
@Time    :   2019/04/16 10:34:28
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program creates a menubar. The menubar has one menu with an exit action.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

# 我们创建了只有一个命令的菜单栏，这个命令就是终止应用。
# 同时也创建了一个状态栏。而且还能使用快捷键Ctrl+Q退出应用。
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # 初始化 调用类的初始化方法
        self.initUI()
        
        
    def initUI(self):               
        
        exitAct = QAction(QIcon('icon.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q') # 设置快捷键组合
        exitAct.setStatusTip('Exit application')
        # QAction是菜单栏, 工具栏或者快捷键的动作的组合. 前面两行, 我们创建了一个图标,
        # 一个exit的标签和一个快捷键组合, 执行了一个动作. 第三行，创建了一个状态栏，
        # 当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct.triggered.connect(qApp.quit)
        # 当执行这个指定的动作时，就触发了一个事件。
        # 这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。

        self.statusBar()
        # 创建状态栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        # menuBar()创建菜单栏。这里创建了一个菜单栏，并在上面添加了一个file菜单，并关联了点击退出应用的事件
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())