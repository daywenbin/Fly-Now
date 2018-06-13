# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 19:07:02 2018

@author: Administrator
"""

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow

from firstpyqt5 import *

if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exec_()