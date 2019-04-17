#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   slider_button_27th.py
@Time    :   2019/04/17 21:08:34
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This example shows a QSlider widget.
'''
# QSlider是个有一个小滑块的组件，这个小滑块能拖着前后滑动,
# 这个经常用于修改一些具有范围的数值, 比文本框或者点击增加减少的文本框(spin box)方便多了
# 本例用一个滑块和一个标签展示。标签为一个图片，滑块控制标签(的值)
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
# 模拟的音量控制器。拖动滑块，能改变标签位置的图片
class Example(QWidget):    
    def __init__(self):
        super().__init__()        
        self.initUI()
               
    def initUI(self):      
        sld = QSlider(Qt.Horizontal, self)
        # 创建一个水平的QSlider
        # QSlider(Qt.Horizontal)
        # Qslider(Qt.Vertical)
        # 详细方法见https://blog.csdn.net/jia666666/article/details/81534588

        sld.setFocusPolicy(Qt.NoFocus)
        # QWidget的setFocusPolicy方法为默认Qt::StrongFocus,
        # 即用户可以通过tab获得焦点，也可以通过鼠标点击(ClickFocus)获得焦点
        # 详情见https://blog.csdn.net/jays_/article/details/83783871
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        # 把valueChanged信号跟changeValue()方法关联起来
        self.label = QLabel(self)
        # 注意文件位置与当前位置
        # 当前位置为工作环境是C:\Users\志君\PycharmProjects\spider
        # 文件环境为C:\Users\志君\PycharmProjects\spider\PyQt5_learn\icon.png
        # 直接写icon.png 默认为C:\Users\志君\PycharmProjects\spider\icon.png, 但是没有
        self.label.setPixmap(QPixmap(r'.\PyQt5_learn\icon.png'))
        # 创建一个QLabel组件并给它设置一个静音图标
        # QPixmap 像素图控件是用来处理图像的控件之一. 它用于将优化后的图像显示在屏幕上
        # 创建的QPixmap 对象需要一个文件地址作为参数 
        # 例如 QPixmap('F:\Python\PyQt5\Widgets\images\****.png')
        # 通过上句把 QPixmap对象映射到的 QLabel 控件
        self.label.setGeometry(260, 40, 500, 500)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap(r'.\PyQt5_learn\mute.jpg'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap(r'.\PyQt5_learn\min.jpg'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap(r'.\PyQt5_learn\med.jpg'))
        else:
            self.label.setPixmap(QPixmap(r'.\PyQt5_learn\max.jpg'))
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())