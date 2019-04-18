#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   photo_qpixmap_30th.py
@Time    :   2019/04/18 19:27:46
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we dispay an image on the window. 
'''
# QPixmap是处理图片的组件. 本例中, 我们使用QPixmap在窗口里显示一张图片. 
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        hbox = QHBoxLayout(self)
        # 水平布局
        pixmap = QPixmap("./PyQt5_learn/icon.jpg")
        # 创建一个QPixmap对象, 接收一个文件作为参数.

        lbl = QLabel(self)
        # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlabel.html#
        # QLabel()的方法API
        lbl.setPixmap(pixmap) # Qlabel的方法
        # 把QPixmap实例放到QLabel组件里

        hbox.addWidget(lbl)
        # QLabel组件加入布局
        self.setLayout(hbox)
        # 设置hbox为整体布局
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())