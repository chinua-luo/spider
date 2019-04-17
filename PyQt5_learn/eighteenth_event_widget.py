#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   eighteenth_event_widget.py
@Time    :   2019/04/17 16:13:19
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we display the x and y coordinates of a mouse pointer in a label widget.
'''
# 事件对象是用python来描述一系列的事件自身属性的对象
# here put the import lib
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

# 这个示例中，我们在一个组件里显示鼠标的X和Y坐标
class Example(QWidget):   
    def __init__(self):
        super().__init__()       
        self.initUI()
               
    def initUI(self):
        # 实例化一个栅格布局           
        grid = QGridLayout()
        grid.setSpacing(10)
        # QGridLayout 里面有两个函数分别是setmargin和setspacing
        # 其中setmargin是设置总的外围边框, setspacing是设置间隔的
        
        # setSpacing(int spacing)
        # setHorizontalSpacing(int spacing)
        # setVerticalSpacing(int spacing) 
        # setSpacing()可以同时设置水平、垂直间距，设置之后，水平、垂直间距相同。 
        # setHorizontalSpacing()、setVerticalSpacing()可以分别设置水平间距、垂直间距。

        x = 0
        y = 0
        # 设置变量
        
        self.text = "x: {0},  y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        # X Y坐标显示在QLabel组件里

        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        # 将label加入布局,位置(0, 0)第一行第一列 ,最后一个是排列方式
        # Qt::AlignTop:垂直方向靠上 Qt::AlignBottom:垂直方向靠下 Qt::AlignVCenter:垂直方向居中 
        # Qt::AlignCenter:等价于Qt::AlignHcenter | Qt::AlignVCenter,即水平和垂直方向都居中

        self.setMouseTracking(True)
        # 事件追踪默认没有开启, 当开启后才会追踪鼠标的点击事件.
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
    # e代表了事件对象. 里面有我们触发事件(鼠标移动)的事件对象.
    # x()和y()方法得到鼠标的x和y坐标点, 然后拼成字符串输出到QLabel组件里 
    def mouseMoveEvent(self, e): 
        x = e.x()
        y = e.y()   
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)
        # 将坐标传入label
          
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())