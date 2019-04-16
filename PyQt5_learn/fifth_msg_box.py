#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   fifth_msg_box.py
@Time    :   2019/04/16 09:30:58
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   This program shows a confirmation message box when we click on the close button of the application window. 
'''
# 默认情况下，我们点击标题栏的 ×按钮，QWidget就会关闭。
# 但是有时候，我们修改默认行为。比如，如果我们打开的是一个文本编辑器，
# 并且做了一些修改，我们就会想在关闭按钮的时候让用户进一步确认操作

# here put the import lib
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
              
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
    # 如果关闭QWidget，就会产生一个QCloseEvent。改变控件的默认行为，就是替换掉默认的事件处理。 
    # 没有被调用呀???  # 继承过来的方法, 重构了
    def closeEvent(self, event):
        # 接收所有的 event 进行如下判断
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        # 我们创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏(message),
        # 第二个字符串显示在对话框, 第三个参数是消息框的俩按钮(QMessageBox.Yes | QMessageBox.No),
        # 最后一个参数是默认按钮, 这个按钮是默认选中的. 返回值在变量reply里。
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        # 这里判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否者就忽略关闭事件.     
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())