#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   second_learn.py
@Time    :   2019/04/16 08:53:21
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''
# here put the import lib
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 创建对象 面向对象编程最重要的三个部分是类(class)、数据和方法。
class Example(QWidget):
    # 我们创建了一个类的调用，这个类继承自QWidget
    # 这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。
    # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
    def __init__(self):
        # QWidget() 初始化同时通过构造器构造了QWidget对象,并将之初始化, 
        # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
        # 默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
        super().__init__() # ex = Example()同时也蕴含着, ex = QWidget()

        # 使用initUI()方法创建一个GUI
        self.initUI()
         
    def initUI(self):
        # 下面的三个方法都继承自QWidget类。
        self.setGeometry(300, 300, 300, 220)
        # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
        self.setWindowTitle('Icon')
        # 我们给这个窗口添加了一个标题，标题在标题栏展示
        self.setWindowIcon(QIcon('icon.jpg'))
        # 此方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。        
        self.show()
        # show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。
    ex = Example()
    sys.exit(app.exec_())
    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，
    # 并把事件传入到派发到应用控件里。当调用exit()方法或直接销毁主控件时，
    # 主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
    # exec_()之所以有个下划线，是因为exec是一个Python的关键字。