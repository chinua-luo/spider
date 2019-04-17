#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   dialog_box_21st.py
@Time    :   2019/04/17 18:25:18
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we receive data from a QInputDialog dialog.
'''
# QInputDialog提供了一个简单方便的对话框, 可以输入字符串, 数字或列表
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
import sys
# 示例有一个按钮和一个输入框, 点击按钮显示对话框, 输入的文本会显示在输入框里
class Example(QWidget):
    def __init__(self):
        super().__init__()       
        self.initUI()
       
    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # 将点击事件与slot函数showDialog链接起来
        self.le = QLineEdit(self)
        # QLineEdit是单行文本编辑控件,是比较基础且常用的控件的之一
        # 更多细节见 https://blog.csdn.net/jia666666/article/details/81510502
        self.le.move(200, 22)
        # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(130, 22)的位置。
        # 第一个数字代表横向(x轴), 第二个数字代表竖直向(y轴)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
               
    def showDialog(self):       
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        # 这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符.
        # 对话框返回输入内容和一个布尔值, 如果点击的是OK按钮, 布尔值就返回True。
        if ok:
            self.le.setText(str(text))
               
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())