#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   fourteen_gridlayout.py
@Time    :   2019/04/16 19:03:44
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we create a skeleton of a calculator using a QGridLayout
'''
# "最常用的还是栅格布局了. 这种布局是把窗口分为行和列. 创建和使用栅格布局, 需要使用QGridLayout模块"
# here put the import lib
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)

# 例子里 创建了栅格化的按钮
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        # 创建一个QGridLayout实例，并把它放到程序窗口里

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        # 将要使用的按钮的名称
        positions = [(i,j) for i in range(5) for j in range(4)]
        # 创建按钮位置列表

        for position, name in zip(positions, names):
            """
            class zip(iter1, iter2...)
            zip(iter1 [,iter2 [...]]) --> zip object
            Return a zip object whose .next() method returns a tuple where the i-th 
            element comes from the i-th iterable argument. 
            The .next() method continues until the shortest iterable in the argument 
            sequence is exhausted and then it raises StopIteration.
            """
            if name == '':  # 跳过这个位置, 下一次position变成下一值
                continue
            button = QPushButton(name) # name为空,会有一个button,只是上面无字
            grid.addWidget(button, *position)
            # 创建按钮，并使用addWidget()方法把按钮放到布局里面
            # QGridLayout::addWidget ( QWidget * widget, int row, int column, Qt::Alignment alignment = 0 )
            # row:行位置
            # column：列位置
            # alignment；对齐方式
            
            # void QGridLayout::addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
            # This is an overloaded function.
            # 6个参数表示控件名，行，列，占用行数，占用列数，对齐方式

            # The *args and **kwargs is a common idiom to allow arbitrary number of arguments 
            # to functions as described in the section more on defining functions 
            # in the Python documentation.
            # The *args will give you all function parameters as a tuple.
            # The **kwargs will give you all keyword arguments except for 
            # those corresponding to a formal parameter as a dictionary.
            # Another usage of the *l idiom is to unpack argument lists when calling a function.

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())