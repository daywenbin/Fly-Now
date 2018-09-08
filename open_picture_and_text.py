# -*- coding: utf-8 -*-

'''
    【简介】
    PyQt5中 QFileDialog 例子
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)
        self.le = QLabel("")
        layout.addWidget(self.le)
        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog 例子")

    def getfile(self):
        '''
        getOpenFileName():返回用户所选择文件的名称，并打开该文件
        第一个参数用于指定父组件
        第二个参数指定对话框标题
        第三个参数指定目录
        第四个参数是文件扩展名过滤器
        '''
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        '''
        setFileMode():
        QFileDialog.AnyFile,任何文件
        QFileDialog.ExistingFile,已存在的文件
        QFileDialog.Directory,文件目录
        QFileDialog.ExistingFiles,已经存在的多个文件
        '''
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        #设置过滤器
        dlg.setFilter( QDir.Files  )

        if dlg.exec_():
            filenames= dlg.selectedFiles()
            f = open(filenames[0], 'r') 

            with f:
                data = f.read()
                self.contents.setText(data) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())