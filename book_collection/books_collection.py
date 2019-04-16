#!/usr/bin/env python # 保证可以直接Unix/Linux/Mac上运行
# -*- encoding: utf-8 -*-
'''
@File    :   books_collection.py
@Time    :   2019/04/15 20:03:11
@Author  :   Lucifer 
@Version :   1.0
@Contact :   chinuagao@gmail.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# 通过程序可以统计手中的实体书, 包括书名,作者,系列, ect
# 可以远程操作
# 将数据储存在 MySQL上database: books, table: real_books, 中英文储存
# "书名:" "作者:" "系列"
# 图形化操作界面

# here put the import lib
import books_collection_setting as bcs
import mysql_interactive as mi

# 因为上面导入就是把模块内容放在相应位置, 后面更改就会变动 ,后面没改的就不会动

bcs.DATA = {
    "name" : '黎曼几何引论(上)',
    "author" : '陈维桓, 李兴霄',
    "list": '北大数学系列丛书',
    "short_desc": ' '
}
# CONDITION = "name like '%几%论%' "
CONDITION = ''
#  

class Window(bcs.QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.langlist = ['压缩','解压']

        self.browseButton = self.createButton("&选择...", self.browse)
        self.transButton = self.createButton("&开始", self.translate)

        self.lang_srcComboBox = self.createComboBox()
        srcIndex = self.langlist.index('压缩')
        self.lang_srcComboBox.setCurrentIndex(srcIndex)
        self.fileComboBox = self.createComboBox('file')

        srcLabel = bcs.QtWidgets.QLabel("压缩or解压:")``
        docLabel = bcs.QtWidgets.QLabel("选择文档:")
        self.filesFoundLabel = bcs.QtWidgets.QLabel()

        self.logPlainText = bcs.QtWidgets.QPlainTextEdit()
        self.logPlainText.setReadOnly(True)


        buttonsLayout = bcs.QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(self.transButton)

        mainLayout = bcs.QtWidgets.QGridLayout()
        mainLayout.addWidget(srcLabel, 0, 0)
        mainLayout.addWidget(self.lang_srcComboBox, 0, 1, 1, 2)
        #mainLayout.addWidget(dstLabel, 1, 0)
        #mainLayout.addWidget(self.lang_dstComboBox, 1, 1, 1, 2)
        #mainLayout.addWidget(docLabel, 2, 0)
        mainLayout.addWidget(self.fileComboBox, 2, 1)
        mainLayout.addWidget(self.browseButton, 2, 2)
        # mainLayout.addWidget(self.filesTable, 3, 0, 1, 3)
        mainLayout.addWidget(self.logPlainText, 3, 0, 1, 3)
        mainLayout.addWidget(self.filesFoundLabel, 4, 0)
        mainLayout.addLayout(buttonsLayout, 5, 0, 1, 3)
        self.setLayout(mainLayout)

        app_icon = bcs.QIcon()#icon = https://imgur.com/NV7Ugfd
        icon_path = resource_path('icon.png')
        app_icon.addFile(icon_path, bcs.QSize(16, 16))
        app_icon.addFile(icon_path, bcs.QSize(24, 24))
        app_icon.addFile(icon_path, bcs.QSize(32, 32))
        app_icon.addFile(icon_path, bcs.QSize(48, 48))
        app_icon.addFile(icon_path, bcs.QSize(256, 256))
        self.setWindowIcon(app_icon)

        self.setWindowTitle("Python压缩")
        self.resize(600, 400)

        # translate
        self.logger = LogHandler()
        self.logger.show.connect(self.onLog)
        zip_console.g_log = self.logger
        self.task = ZipTask()
        self.task.done.connect(self.onLog)


    def compress_procedure(self):
        dialog = FileDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            pass
        sfile = dialog.selectedFiles()
        print('select compress file:',sfile)

        if sfile:
            self.logPlainText.clear()
            msg = '选择了要压缩的文件: <b>{}</b>'.format(sfile)
            self.logger.show.emit(msg)
            if self.fileComboBox.findText(sfile) == -1:
                self.fileComboBox.addItem(sfile)

            self.fileComboBox.setCurrentIndex(self.fileComboBox.findText(sfile))
    
    def uncompress_procedure(self):
        sfile, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "选择文件",
            QtCore.QDir.currentPath(),
            "(*.zip *.rar)",
        )
        print(sfile)
        if sfile:
            self.logPlainText.clear()
            msg = '选择了要解压的文件: <b>{}</b>'.format(sfile)
            self.logger.show.emit(msg)
            if self.fileComboBox.findText(sfile) == -1:
                self.fileComboBox.addItem(sfile)

            self.fileComboBox.setCurrentIndex(self.fileComboBox.findText(sfile))

    def browse(self):
        lang_src_select = self.lang_srcComboBox.currentText()
        print('lang_src_select:', lang_src_select)
        if '压缩' == lang_src_select:
            self.compress_procedure()
            self._flg = 1
        else:
            self.uncompress_procedure()
            self._flg = 2

    def onLog(self, msg):
        self.logPlainText.appendHtml(msg)

    def translate(self):
        fileName = self.fileComboBox.currentText()
        if not fileName:
            self.logger.show.emit('请先选择要压缩或解压的文件')
            return
        print(fileName)
        self.logger.show.emit('开始执行：{}'.format(fileName))
        self.task.set_attr(fileName,self._flg)
        self.task.start()

    def createButton(self, text, member):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, btype=''):
        comboBox = QtWidgets.QComboBox(self)
        if btype != 'file':
            comboBox.setEditable(True)
            comboBox.addItems(self.langlist)
        comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Preferred)
        return comboBox




if __name__ == "__main__":
    db = bcs.pymysql.connect(host='localhost', user="root",
                       password="Luozhijun199502@", port=3306, db="books")  # 端口默认3306 需要指定数据库
    coursor = db.cursor()  # 获取游标
    my = mi.interactive(db)
    my.select(CONDITION)
    db.close()
    # 主程序
