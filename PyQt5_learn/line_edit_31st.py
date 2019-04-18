#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   line_edit_31st.py
@Time    :   2019/04/18 19:44:14
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This example shows text which is entered in a QLineEdit in a QLabel widget
'''
# QLineEdit组件提供了编辑文本的功能，自带了撤销、重做、剪切、粘贴、拖拽等功能
# here put the import lib
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QLineEdit, QApplication)

# 例子中展示了一个编辑组件和一个标签，我们在输入框里键入的文本，会立即在标签里显示出来
class Example(QWidget):   
    def __init__(self):
        super().__init__()        
        self.initUI()
               
    def initUI(self):      
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        # 创建一个QLineEdit对象
        
        qle.move(60, 100)
        self.lbl.move(60, 40)
        # 调节位置
        qle.textChanged[str].connect(self.onChanged)  # textChanged有返回值
        # 如果输入框的值有变化，就调用onChanged()方法
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
               
    def onChanged(self, text):        
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # 在onChanged()方法内部，我们把文本框里的值赋值给了标签组件, 
        # 然后调用adjustSize()方法让标签自适应文本内容    
        
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())