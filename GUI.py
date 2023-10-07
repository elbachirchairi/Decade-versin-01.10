#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
# import os
import glob
import sys
import os
from datetime import datetime
import locale
from PyQt5 import QtCore, QtWidgets, QtPrintSupport, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor, QIcon, QKeySequence, QColor, QTextCharFormat, QTextDocument, QTextFormat, \
    QFontDatabase
from PyQt5.QtWidgets import *
import time
from PyQt5 import QtWidgets
# import subprocess
# from PyQt5 import uic  # added
from PyQt5.QtCore import QDate,QTime
from datetime import datetime
import datetime
from datetime import datetime
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import openpyxl
import pandas as pd
from PyQt5 import QtWidgets, QtGui
import src
import datetime
import numpy as np
import os
from src.py.navire import navire
from PyQt5.uic import loadUi
from openpyxl.workbook import Workbook
import os
import re
import glob
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Alignment, Border, Side, Font
from openpyxl.styles import Alignment, Font
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
import shutil


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('src/ui/décade.ui', self)
        self.filepath = None
        self.dirpaths = []
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 140)
        self.tableWidget_2.setColumnWidth(0, 70)
        self.tableWidget_2.setColumnWidth(1, 140)
        self.tableWidget_3.setColumnWidth(0, 190)
        self.tableWidget_3.setColumnWidth(1, 200)
        self.tableWidget_3.setColumnWidth(2, 110)
        self.tableWidget_3.setColumnWidth(3, 95)
        self.pushButton_2.clicked.connect(self.addlin)
        self.pushButton_3.clicked.connect(self.romovlin)

    def romovlin(self):
        """row = self.tableWidget_3.rowCount()
        self.tableWidget_3.removeRow(row-1)"""
        """if row >= 0:  # Assurez-vous qu'une ligne est sélectionnée ou que vous souhaitez supprimer
            self.tableWidget_3.removeRow(row)  # Supprimez la ligne"""
        selected_row = self.tableWidget_3.currentRow()  # Obtenez le numéro de la ligne sélectionnée
        if selected_row >= 0:
            self.tableWidget_3.removeRow(selected_row)


    def addlin(self):
        row = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row)



if __name__ == '__main__':
    my_app = QtWidgets.QApplication(sys.argv)
    my_window = MyApp()
    my_window.show()
    my_window.setStyleSheet(
        # "QPushButton { background-color: palegoldenrod; border-width: 2px; border-color: darkkhaki}"
        # "QPushButton { border-style: solid; border-radius: 5; padding: 3px; min-width: 9ex; min-height: 2.5ex;}"
        # "QLabel, QAbstractButton { font: bold; font-size: 9px }"
        "QPushButton#evilButton { background-color: palegoldenrod;border-style: outset;border-width: 2px;border-radius: 10px;border-color: darkkhaki ;font: bold 14px;min-width: 10em;padding: 6px}"
        "QToolButton#evilButton { background-color: palegoldenrod;border-style: outset;border-width: 2px;border-radius: 10px;border-color: darkkhaki ;font: bold 14px;min-width: 10em;padding: 6px}"
        #"QStatusBar QLabel { font: normal }"
        "QStatusBar::item { border-width: 1; border-color: darkkhaki; border-style: solid; border-radius: 2;}"
        "QLineEdit, QSpinBox, QTextEdit, QListView { background-color: cornsilk; selection - color: #0a214c}"
        " QLineEdit, QSpinBox, QTextEdit, QListView { selection-background-color:  #C19A6B;}"
        "QLineEdit, QFrame { border-width: 1px; border-style: solid; border-color: darkkhaki; border-radius: 5px}"
        "QLabel { border: none; padding: 0; background: none; }"
        "QMenuBar {background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightgray, stop:1 #FFFDE2);spacing: 3px; /* spacing between menu bar items */}"
        "QPlainTextEdit {font-family: Monospace; font-size: 13px; background:  #E2E2E2; color:  #202020; border: 1px solid #1EAE3D;}")
    sys.exit(my_app.exec())