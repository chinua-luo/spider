#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   sixth_center_window.py
@Time    :   2019/04/16 09:42:25
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program centers a window on the screen.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(1000, 600)
        # resize()方法能改变控件的大小，这里的意思是窗口宽1000px，高600px
        self.center()
        # 调用下面  
        
        self.setWindowTitle('Center')    
        self.show()
        
        
    def center(self):    
        qr = self.frameGeometry()
        # 得到了主窗口的大小 PyQt5.QtCore.QRect(0, 0, 999, 599)  前两位为左上角坐标 后两位为主窗口大小
        cp = QDesktopWidget().availableGeometry().center()
        # 获取显示器的分辨率，然后得到中间点的位置
        qr.moveCenter(cp)
        # 然后把自己窗口的中心点放置到qr的中心点。
        self.move(qr.topLeft())
        # 然后把窗口的左上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
