#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   eleventh_textmenu.py
@Time    :   2019/04/16 13:05:52
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This program creates a context menu.
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

# 使用contextMenuEvent()方法实现这个菜单
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()
    
    # 父类继承的方法 重构 右键出现菜单
    def contextMenuEvent(self, event):
           cmenu = QMenu(self)
           # 新建菜单 ,在此方法内的菜单都会出现在右键菜单中
           newAct = cmenu.addAction("新建") 
           opnAct = cmenu.addAction("打开")
           quitAct = cmenu.addAction("退出")
           # 加入空白action, 
           action = cmenu.exec_(self.mapToGlobal(event.pos()))
           # 使用exec_()方法显示菜单. 从鼠标右键事件对象中获得当前坐标。
           # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标
           if action == quitAct:
               qApp.quit()
            # 如果右键菜单里触发了事件，也就触发了退出事件，执行关闭菜单行为
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())