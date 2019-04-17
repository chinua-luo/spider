#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   color_background_22ed.py
@Time    :   2019/04/17 18:42:21
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we select a color value from the QColorDialog and change the background color of a QFrame widget.
'''
# QColorDialog提供颜色的选择
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys
# 例子里有一个按钮和一个QFrame,
# 默认的背景颜色为黑色, 我们可以使用QColorDialog改变背景颜色。
class Example(QWidget):   
    def __init__(self):
        super().__init__()        
        self.initUI()
               
    def initUI(self):      
        col = QColor(0, 0, 0) 
        # 初始化QtGui.QFrame的背景颜色 rgb
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # 将点击事件与slot函数showDialog链接起来
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        # 设置QWidget背景色
        # setStyleSheet() 具体百度吧
        # 1. 该函数只能用于设置有父窗口的子窗口的背景！如果一个窗口没有父窗口, 
        # 则无法使用该函数来设置背景颜色或图片
        #  2. 同时: 对于一个父窗口而言: 如果我们用setStyleShette设置了其样式, 
        # 而对于其子窗口: 如果没有用同样的函数来设置的话, 则其子窗口的样式和其父窗口完全一致,
        # 亦即: 其集成了自己父窗口的样式！
        #  3. 延伸:对顶层窗口(没有父窗口), 其有若干个子窗口，则当我们用setStyleShette来设置这个
        # 顶层窗口的样式后, 依据1可知:该父窗口本身没有任何变化, 亦即设置没有生效; 
        # 而其子窗口：只要子窗口本身没有用setStyleShette来设置自己的样式表, 
        # 则其就是用的自己父窗口的样式表
        self.frm.setGeometry(230, 22, 100, 100)
        # 设置frame框架大小(后两位) 位置(前两位)           
        
        self.setGeometry(600, 600, 1000, 600)
        # setGeometry()有两个作用：把窗口放到屏幕上位置(前两个)并且设置窗口大小(后两个)
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽,高也就是说这个方法是resize()和move()的合体.
        self.setWindowTitle('Color dialog')
        self.show()
              
    def showDialog(self):     
        col = QColorDialog.getColor()
        # 弹出一个QColorDialog对话框
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
        # 我们可以预览颜色，如果点击取消按钮，没有颜色值返回,
        # 如果颜色是我们想要的，就从取色框里选择这个颜色
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())