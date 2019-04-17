#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   font_23rd.py
@Time    :   2019/04/17 19:31:20
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   In this example, we select a font name and change the font of a label.
'''
# 创建了一个有一个按钮和一个标签的QFontDialog的对话框, 我们可以使用这个功能修改字体样式
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
import sys

class Example(QWidget):   
    def __init__(self):
        super().__init__()      
        self.initUI()
               
    def initUI(self):      
        vbox = QVBoxLayout()
        # 垂直布局
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        # 控件在布局中,设置才有效. 两个参数分别是水平和竖直扩展性. 默认都是可扩展
        # setSizePolicy 是设置控件在布局（layout）里面的大小变化的属性. 如果控件没有在布局里，没什么用。
        # 默认情况下，把 widget放入layout, widget的大小一定程度上会随着 layout 变大而变大或者缩小而缩小;
        # 可以设置 widget 的 sizePolicy、minmunSize 和 maxmumSize，使其一定程度上不受 layout 的影响，
        # 但是不是说设置了 widget 的最小高度后，widget就一定能显示这么大的高度, 当 layout 减小到比 widget 
        # 最小高度更小的尺寸，widget 显示的不是按比例缩小，而是不完全显示。
        # 把几个 widget 放入 layout 里面，可以通过设置 widget 的 sizePolicy、minmumSize 和 
        # maxmumSize，layout 的 layoutStretch 和 layoutSpacing，从而控制 widget 的大小和相对位置.
        # QSizePolicy的说明
        # This property holds the default layout behavior of the widget.
        # If there is a QLayout that manages this widget's children, the size policy specified
        # by that layout is used. If there is no such QLayout, the result of this function is used
        # Fixed: 大小不能改变
        # Minimum: 已经是最小, 不能再被缩小, 但能放大.
        # Maximum: 已经是最大, 不能再被放大, 但能缩小.
        # Preferred:  控件的sizeHint()是他的sizeHint, 能被缩小, 放大.
        # Expanding: 控件可以自行增大或者缩小.

        btn.move(20, 20)
        vbox.addWidget(btn)
        # 将btn加入到vbox布局中
        btn.clicked.connect(self.showDialog)
        # 将btn与showDialog链接到一起
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        # 将lbl加入到vbox布局中
        self.setLayout(vbox)          
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
        
    def showDialog(self):
        # 弹出一个字体选择对话框. getFont()方法返回一个字体名称和状态信息. 状态信息有OK和其他两种
        font, ok = QFontDialog.getFont() # ok 有False和True两种, 确认就为True
        if ok:
            self.lbl.setFont(font)
            # 将lbl字体改变
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())