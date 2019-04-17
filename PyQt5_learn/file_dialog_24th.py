#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   file_dialog_24th.py
@Time    :   2019/04/17 19:49:43
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we select a file with a QFileDialog and display its contents in a QTextEdit.
'''
# QFileDialog给用户提供文件或者文件夹选择的功能。能打开和保存文件
# here put the import lib
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
# 本例中有一个菜单栏, 一个置中的文本编辑框, 一个状态栏. 点击菜单栏选项会弹出一个
# QtGui.QFileDialog对话框，
# 在这个对话框里, 你能选择文件, 然后文件的内容就会显示在文本编辑框里
class Example(QMainWindow):  
    def __init__(self):
        super().__init__()       
        self.initUI()
    # 这里设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的

    def initUI(self):      
        self.textEdit = QTextEdit()
        # QTextEdit类是一个多行文本框控件，可以显示多行文本内容, 当文本内容超出控件显示范围时, 
        # 可以显示水平个垂直滚动条，Qtextedit不仅可以用来显示文本还可以用来显示HTML文档
        # 基本方法见https://blog.csdn.net/jia666666/article/details/81511435
        self.setCentralWidget(self.textEdit)
        # void QMainWindow::setCentralWidget (QWidget * widget )
        # 它将把widget设置为主窗口的中心窗口部件
        # 每次程序调用setCentralWidget()方法时，先前存在的中心窗口部件将被新的所替换,
        # 而且主窗口会销毁原来的部件，无需用户处理
        self.statusBar() # 状态栏

        openFile = QAction(QIcon('icon.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        # 打开文件的行为

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        # 创建菜单, 并绑定打开文件行为     
        
        self.setGeometry(300, 300, 1000, 600)
        # setGeometry()有两个作用：把窗口放到屏幕上位置(前两个)并且设置窗口大小(后两个)
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽,高也就是说这个方法是resize()和move()的合体.
        self.setWindowTitle('File dialog')
        self.show()
            
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.') # 读取当前目录
        # 弹出QFileDialog窗口. getOpenFileName()方法的第一个参数是说明文字, 
        # 第二个参数是默认打开的文件夹路径. 默认情况下显示所有类型的文件
        # fname = ('C:/Users/志君/PycharmProjects/spider/baike.html', 'All Files (*)')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf8') as f:
                data = f.read()
                self.textEdit.setText(data)
        # 读取选中的文件，并显示在文本编辑框内(打开HTML文件时,是渲染后的结果)        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())