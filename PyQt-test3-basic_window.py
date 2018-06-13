# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:16:39 2018

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    w = QWidget()
    w.resize(200,200)
    w.move(540,284)
    w.show()
    sys.exit(app.exec_())
    