#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   seventeenth_reimplement_event_handler.py
@Time    :   2019/04/17 16:02:59
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we reimplement an event handler.
'''
# here put the import lib
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

# 此例我们替换了事件处理器函数keyPressEvent()
class Example(QWidget):  
    def __init__(self):
        super().__init__()   
        self.initUI()    
        
    def initUI(self): # 初始化函数          
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):  # e是event, 自动捕捉到的,然后就调用这个函数
        # event是Qt.Key_Escape就退出. 不是,什么也不发生    
        if e.key() == Qt.Key_Escape:
            self.close()
        # 如果按下ESC键程序就会退出
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())