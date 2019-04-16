#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   nineth_submenu.py
@Time    :   2019/04/16 11:38:12
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program creates a submenu.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

# 这个例子里，有两个子菜单，一个在file菜单下面，一个在file的import下面
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        # menuBar()创建菜单栏,
        fileMenu = menubar.addMenu('File')
        # 这里创建了一个菜单栏，并在上面添加了一个file菜单

        impMenu = QMenu('Import', self)
        # 使用QMenu创建一个新菜单。

        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)
        # 使用addAction添加一个动作。

        newAct = QAction('New', self)        
        
        fileMenu.addAction(newAct)
        # 添加一个行为(未关联事件的行为)
        fileMenu.addMenu(impMenu)
        #  嵌套添加菜单
        
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Submenu')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())