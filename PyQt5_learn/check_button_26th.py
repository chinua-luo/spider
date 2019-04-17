#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   check_button_26th.py
@Time    :   2019/04/17 20:46:27
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we create three toggle buttons. They will control the background color of a QFrame.
'''
# 切换按钮就是QPushButton的一种特殊模式. 它只有两种状态：
# 按下和未按下. 我们再点击的时候切换两种状态, 有很多场景会使用到这个功能
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys
# 创建了一个切换按钮和一个QWidget, 并把QWidget的背景设置为黑色.
# 点击不同的切换按钮, 背景色会在红、绿、蓝之间切换(而且能看到颜色合成的效果，而不是单纯的颜色覆盖)
class Example(QWidget):    
    def __init__(self):
        super().__init__()       
        self.initUI()
             
    def initUI(self):      
        self.col = QColor(0, 0, 0)       
        # 设置颜色为黑色
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        # 创建一个QPushButton, 然后调用它的setCheckable()的方法就把这个按钮变成了切换按钮

        redb.clicked[bool].connect(self.setColor)
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值
        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        # 调用它的setCheckable()的方法就把这个按钮变成了切换按钮
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值
        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        # 调用它的setCheckable()的方法就把这个按钮变成了切换按钮
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()
        
        
    def setColor(self, pressed):       
        source = self.sender()
        # 获取被点击的按钮
        if pressed:
            val = 255
        else:
            val = 0
                        
        if source.text() == "Red":
            self.col.setRed(val)
            # print(self.col.name()) # #ff0000  16进制red  255
            # 只是把red的值改为val   rgb三个值()
            # 如果是标签为“red”的按钮被点击，就把颜色更改为预设好的对应颜色                
        elif source.text() == "Green":
            self.col.setGreen(val)
            # print(self.col.name()) # #00ff00  16进制 green   255                      
        else:
            self.col.setBlue(val)
            # print(self.col.name()) # #0000ff  16进制 blue   255
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        # 使用样式表（就是CSS的SS）改变背景色 
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())