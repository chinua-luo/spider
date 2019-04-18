#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   progressbar_28th.py
@Time    :   2019/04/18 00:04:06
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2019
@Desc    :   This example shows a QProgressBar widget.
'''
# 进度条是用来展示任务进度的, 它的滚动能让用户了解到任务的进度.
# QProgressBar组件提供了水平和垂直两种进度条, 进度条可以设置最大值和最小值，
# 默认情况是0~99
# here put the import lib
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer, Qt
import sys
# 创建了一个水平的进度条和一个按钮，这个按钮控制进度条的开始和停止
class Example(QWidget):   
    def __init__(self):
        super().__init__()        
        self.initUI()
               
    def initUI(self):      
        self.pbar = QProgressBar(self)
        # 新建(实例化)一个QProgressBar构造器
        # self.pbar.setRange(a,b) 设置最大和最小值, 即取值范围
        # setMaximum() setMinimum() 单独设置
        self.pbar.setMaximum(4000)
        # 不论最大值最小值设置为多少, 界面显示为 (Value- minimum)/(maximum - minimum) 加个 %
        # 最大最小值主要用来调控当前最大值完成的程度为多少或者改变不同情况下进度条速度, 本例中就改变了进度条运行的速度
        # self.pbar.setOrientation(Qt.Vertical) # 可用, 没问题 不过需要调改一下进度框的方向
        self.pbar.setGeometry(30, 40, 200, 25)
        # 设置该QProgressBar构造器的位置(前两个), 和大小(后两个)
        


        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        # QBasicTimers 是一个很快的、轻量级的定时器类，它主要被Qt内部使用。
        # 所以，我们一般不建议在上层应用程序中直接使用这个类去做定时器工作。
        # 在开发应用程序时，我们一般推荐使用QTimer类和QObject的成员函数startTimer来启动定时器
        # QBasicTimer定时器是一种重复性定时器，即它在启动后会不断的向应用程序发送定时器事件，
        # 直到你收到调用stop() 时才停止
        self.step = 0
        # 设置计步器
        
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('QProgressBar')
        self.show()
    
    # 重构父类时间事件处理方法  捕捉时间事件,一旦有变化就执行此方法      
    def timerEvent(self, e):
        if self.step >= 4000:
            self.timer.stop()
            self.btn.setText('Finished')
            self.pbar.setValue(self.step)
            return           
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        # 默认情况是0~99
        
        

    def doAction(self):
        # 通过时间来控制, 每按一次button调用该函数, 判断定时器状态, 决定按后定时器状态
        # self.timer.isActive()
        # true:定时器处于工作状态中
        # false: 定时器不处于工作状态
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            # 调用start()方法, 启动定时器(按下)
            # void QBasicTimer::start(int msec, QObject *object) 
            # msec: 定时时间间隔(毫秒 1000ms = 1s),(每过一个此时时间间隔, QBasicTimer便会发出一个时间事件), *object接受定时器事件的对象
            self.btn.setText('Stop')
                  
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())