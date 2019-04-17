#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   nineteenth_sender.py
@Time    :   2019/04/17 18:11:16
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we determine the event sender object.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

# 有时候我们会想知道是哪个组件发出了一个信号, PyQt5里的sender()方法能搞定这件事(决定事件源)
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
        # (俩个button)
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        # 将button与buttonClicked连接起来 两个按钮都和同一个slot绑定
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    # buttonClicked()方法决定了是哪个按钮能调用sender()方法
    def buttonClicked(self): 
        sender = self.sender()
        # 我们用调用sender()方法的方式决定了事件源
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())