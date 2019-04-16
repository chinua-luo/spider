#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   tenth_checkable_menu.py
@Time    :   2019/04/16 11:48:19
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program creates a checkable menu.

'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

# 本例创建了一个行为菜单. 这个行为／动作能切换状态栏显示或者隐藏。
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
        # 创建菜单栏, 并添加菜单view
        
        viewStatAct = QAction('View statusbar', self, checkable=True)
        # 用checkable选项创建一个能选中的菜单
        viewStatAct.setStatusTip('View statusbar')  # 状态栏提示
        viewStatAct.setChecked(True)
        # 默认设置为选中状态。
        viewStatAct.triggered.connect(self.toggleMenu)
        # connect(slot[, type=PyQt5.QtCore.Qt.AutoConnection[, no_receiver_check=False]])
        # Parameters: 
        # slot – the slot to connect to, either a Python callable or another bound signal.
        # type – the type of the connection to make.
        # no_receiver_check – suppress the check that the underlying C++ receiver instance still exists and deliver the signal anyway.
        # 事件关联行为
        viewMenu.addAction(viewStatAct)
        # 将行为加入菜单

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()
        
    def toggleMenu(self, state):  # state是怎么传过来的
        # 依据选中状态切换状态栏的显示与否 两种行为
        if state:
            self.statusbar.show() 
        else:
            self.statusbar.hide()
       
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())