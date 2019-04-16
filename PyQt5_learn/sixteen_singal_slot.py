#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   sixteen_singal_slot.py
@Time    :   2019/04/16 23:45:52
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we connect a signal of a QSlider to a slot of a QLCDNumber.
'''
# here put the import lib
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


class Example(QWidget):  
    def __init__(self):
        super().__init__()       
        self.initUI()
               
    def initUI(self):
        
        lcd = QLCDNumber(self)
        # QLCDNumber控件用于显示一个带有类似液晶显示屏效果的数字
        # 它可以显示几乎任何尺寸的数字, 同时支持显示十进制，十六进制，八进制或二进制数. 
        # 使用display() 槽可以容易地连接到数据源
        sld = QSlider(Qt.Horizontal, self)
        # QSlider控件提供一个垂直或者水平的滑动条，滑动条是一个用于控制有界值典型的控件，
        # 它允许用户沿水平或者垂直方向在某一范围内移动滑块，并将滑块所在的位置转换为一个
        # 合法范围内的整数值，有时候这中方式比输入数字或者使用SpinBox（计数器·）更加自然,
        # 在槽函数中对滑块所在位置的处理相当于从整数之间的最小值和最高值进行取值

        # 显示了QtGui.QLCDNumber和QtGui.QSlider模块, 我们能拖动滑块让数字跟着发生改变

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        # 这里是把滑块的变化和数字的变化绑定在一起
        # sender(sld.valueChanged)是信号的发送者，receiver(lcd)是信号的接收者，slot(lcd.display)是对这个信号应该做出的反应
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('Signal and slot')
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())