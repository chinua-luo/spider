#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   twelve_checkbox.py
@Time    :   2019/04/16 18:14:11
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   None
'''

# class QCheckBox(QAbstractButton)
#  |  QCheckBox(QWidget parent=None)
#  |  QCheckBox(str, QWidget parent=None)
"""
由此可见QCheckBox继承自QAbstractButton。 
同QRadioButton,QCheckBox也是一个开关按钮，可切换状态on或者off，即checked或者unchecked.
一般，此复选框可以enable或者disable但不影响其他复选按钮。但是如果此放置到一个互斥的QButtonGroup里面，
则只能选一个复选框。这是由互斥选项的QButtonGroup所限定的属性。 
当checkbox复选框是checked标记或者清楚, 都会触发stateChangeed信号. 可以使用isChecked()去查询复选框按钮是否
标记。除了常用的选中与没选中状态，QCheckBox提供第三种状态即“没有改变”状态. 如果使用此状态, 
设置其属性setTristate(),然后用checkState()去查询当前标记切换的状态。
"""
# here put the import lib
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGroupBox, QStyleFactory, QVBoxLayout, QTextBrowser
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CheckBox(QWidget):
    def __init__(self):
        super(CheckBox,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CheckBox")
        self.setGeometry(400,400,300,260)

        groupBox = QGroupBox("Non-Exclusive Checkboxes")
        groupBox.setFlat(True)

        self.checkBox1 = QCheckBox("&Checkbox 1")
        self.checkBox2 = QCheckBox("&Checkbox 2")
        self.checkBox2.setChecked(True)
        # 实例化checkBox1和checkBox2两个对象, 并将checkBox2的状态设定为选中状态.
        # 设定快捷键的另外一种方式, 使用“&”符号，如“&Checkbox 1”, 则通过Alt+“c”可以完成鼠标点击对应的行为。
        self.tristateBox = QCheckBox("Tristate button")
        self.tristateBox.setTristate(True)
        self.tristateBox.setCheckState(Qt.PartiallyChecked)
        # 实例化tristateBox 对象； 
        # setTristate(),设定tristateBox 对象是否为三个状态. ”True”,设定为三个状态. 
        # setCheckState(), 设定checkBox的状态, 具体状态如下： 
        # Qt.Unchecked 0    The item is unchecked. 
        # Qt.PartiallyChecked 1    The item is partially checked. Items in hierarchical(等级制度) models may be partially checked if some, but not all, of their children are checked. 
        # Qt.Checked 2    The item is checked.

        self.checkBox1.stateChanged.connect(self.changeCheckBoxStatus)
        self.checkBox2.stateChanged.connect(self.changeCheckBoxStatus)
        self.tristateBox.stateChanged.connect(self.changeCheckBoxStatus)
        # stateChanged(), QCheckBox状态改变时的信号. 在信号发生改变的时候触发自定义的函数changeCheckBoxStatus()

        vbox = QVBoxLayout()
        vbox.addWidget(self.checkBox1)
        vbox.addWidget(self.checkBox2)
        vbox.addWidget(self.tristateBox)
        # 创建一个vbox的垂直布局(QVBoxLayout)并加入checkBox1, checkBox2 widget
        vbox.addStretch(1)
        # void QBoxLayout::addStretch(int stretch = 0)
        # Adds a stretchable space (a QSpacerItem) with zero minimum size and stretch factor stretch 
        # to the end of this box layout.
        # 函数的作用是在布局器中增加一个伸缩量, 里面的参数表示QSpacerItem的个数，默认值为零，
        # 会将你放在layout中的空间压缩成默认的大小.
        # 例如：一个layout布局器, 里面有三个控件, 一个放在最左边, 一个放在最右边, 最后一个放在layout的1/3处，
        # 这就可以通过addStretch去实现。
        groupBox.setLayout(vbox)
        

        self.lcd = QTextBrowser() # 实例化一个对象
        self.lcd.setFixedHeight(190)
        self.lcd.setFont(QFont("Microsoft YaHei", 20))
        self.lcd.setText(self.getCheckBoxStatus())

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(self.lcd)
        self.setLayout(mainLayout)
        # 创建一个mainLayout 的垂直布局(QVBoxLayout)，在 mainLayout 加入widget groupBox与self.lcd

    def changeCheckBoxStatus(self):
        self.lcd.setText(self.getCheckBoxStatus())
    def getCheckBoxStatus(self):
        status = self.checkBox1.text()+":  "+ str(self.checkBox1.checkState()) +"\n" +self.checkBox2.text()+":  "+ str(self.checkBox2.checkState()) \
                 +"\n"+self.tristateBox.text()+":  "+ str(self.tristateBox.checkState())
        return status


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckBox()
    ex.show()
    sys.exit(app.exec_()) 