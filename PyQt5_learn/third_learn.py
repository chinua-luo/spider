#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   third_learn.py
@Time    :   2019/04/16 09:12:20
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)

from PyQt5.QtGui import QFont    


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        # 这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。

        self.setToolTip('This is a <b>QWidget</b> widget')
        # 调用setTooltip()创建提示框可以使用富文本格式的内容

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 创建一个按钮，并且为按钮添加了一个提示框。
        
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        # 调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Tooltips')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())