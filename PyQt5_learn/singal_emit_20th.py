#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   singal_emit_20th.py
@Time    :   2019/04/17 18:17:40
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we show how to emit a custom signal.
'''
# QObject实例能发送事件信号。下面的例子是发送自定义的信号
# here put the import lib
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# 创建了一个叫closeApp的信号, 这个信号会在鼠标按下的时候触发, 事件与QMainWindow绑定
class Communicate(QObject):
    # Communicate类创建了一个pyqtSignal()属性的信号  
    closeApp = pyqtSignal() 

class Example(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.initUI()
    
    def initUI(self):      
        self.c = Communicate()
        self.c.closeApp.connect(self.close)       
        # closeApp信号QMainWindow的close()方法绑定

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    # QMainWindow的mousePressEvent()方法重构
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
    # 点击窗口的时候，发送closeApp信号，程序终止 
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())