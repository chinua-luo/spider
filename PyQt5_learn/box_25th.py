#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   box_25th.py
@Time    :   2019/04/17 20:12:20
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, a QCheckBox widget is used to toggle the title of a window.
'''
# 控件就像是应用这座房子的一块块砖。PyQt5有很多的控件，
# 比如按钮，单选框，滑动条，复选框等等. 
# 
# 在本章，我们将介绍一些很有用的控件：QCheckBox，ToggleButton，QSlider，QProgressBar
# 和 QCalendarWidget
# QCheckBox组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景
# here put the import lib
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys
# 有一个能切换窗口标题的单选框
class Example(QWidget):    
    def __init__(self):
        super().__init__()        
        self.initUI()
                
    def initUI(self):      
        cb = QCheckBox('Show title', self)
        # 这个是QCheckBox的构造器
        cb.move(20, 20)
        cb.toggle()
        # 要设置窗口标题, 我们就要检查单选框的状态. 默认情况下, 窗口没有标题, 单选框未选中
        cb.stateChanged.connect(self.changeTitle)
        # 把changeTitle()方法和stateChanged信号关联起来. 这样, changeTitle()就能切换窗口标题了
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox') # 最开始的标题, 有事件发生就会改变
        self.show()
               
    def changeTitle(self, state):      
        if state == Qt.Checked:
            self.setWindowTitle('QCheckedBox')
        else:
            self.setWindowTitle(' ')
    # 控件的状态是由changeTitle()方法控制的, 如果空间被选中, 
    # 我们就给窗口添加一个标题, 如果没被选中, 就清空标题. 
                  
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())