#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   thirteen_boxlayout.py
@Time    :   2019/04/16 18:46:21
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we position two push buttons in the bottom-right corner  of the window. 
'''
# 例子完成了在应用的右下角放了两个按钮的需求. 当改变窗口大小的时候,
# 它们能依然保持在相对的位置。
# here put the import lib
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 这是创建了两个按钮。
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 不加此句,两个button平均占满横向, 在水平拉伸时会等比例变大
        # 加上此句, 两button会靠后并列, 拉伸时,平移向右移动
        # 里面数字貌似多少不影响
        # 加在button前,将button后移
        # 加在button后, 前button大小位置不动
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # 创建一个水平布局，增加两个按钮和弹性空间.
        # stretch函数在两个按钮前面增加了一些弹性空间

        vbox = QVBoxLayout()
        vbox.addStretch(1) # 不加此句, 水平布局会靠右居中 
        vbox.addLayout(hbox)
        
        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面
        # 弹性元素会把所有的元素一起都放置在应用的右下角。

        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())