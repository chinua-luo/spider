#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   fifteen_feedback_msg.py
@Time    :   2019/04/16 23:33:22
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we create a more complicated window layout using the QGridLayout manager.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication)
# 创建了一个有三个标签的窗口。两个行编辑和一个文版编辑，这是用QGridLayout模块搞定的
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        # 三个标签
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        # 两个行编辑和一个文版编辑窗口

        grid = QGridLayout()
        grid.setSpacing(10)
        # 创建标签之间的空间

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        # 我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示
        # void QGridLayout::addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
        # This is an overloaded function.
        # 6个参数表示控件名，行，列，占用行数，占用列数，对齐方式(默认为0)
        self.setLayout(grid) 
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Review')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())