#!/usr/bin/python

# simple.py

#!/usr/bin/python

# simple.py
import sys
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QStyle, QAction, QMenu
from PySide2.QtGui import QIcon, QCursor
import PySide2.QtCore  as QtCore
from PySide2 import QtGui, QtCore
# from PySide.QtGui import *
# from PySide.QtCore import *
# cross platform copy/paste
# pip3 install pyperclip
# import pyperclip
# 
 
class Window(QMainWindow):
    def __init__(self):
        # super().__init__()
 
        # self.setWindowTitle("Awesome xMenu")
        # self.setGeometry(2500,300,500,400)
        
        # Transparent Window background
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setStyleSheet("background:transparent;")
 
        # menu = self.createDockWindows()
        # menu = self.createPopupMenu()
        # menu.addAction('sdf')
 
        # print('column(%d)' % self.table.horizontalHeader().logicalIndexAt(pos))
        menu = QMenu()
        menu.addAction('Add')
        menu.addAction('Delete')
        menu.exec_(QCursor.pos())
 
        # self.show()
 
    # def create_menu(self):
    #     mainMenu = self.menuBar()
    #     fileMenu = mainMenu.addMenu("&All Icons")

    def exit_app(self):
        self.close()
 
    # def handleHeaderMenu(self, pos):
    #     print('column(%d)' % self.table.horizontalHeader().logicalIndexAt(pos))
    #     menu = QtGui.QMenu()
    #     menu.addAction('Add')
    #     menu.addAction('Delete')
    #     menu.exec_(QtGui.QCursor.pos())
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)
