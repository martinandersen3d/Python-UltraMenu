#!/usr/bin/python

# simple.py

#!/usr/bin/python

# simple.py
import sys
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QStyle, QAction, QMenu
from PySide2.QtGui import QIcon, QCursor
import PySide2.QtCore  as QtCore
from PySide2 import QtGui, QtCore

objectList = {}

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.create_menu()
        self.add_directory('&Scripts')
        self.add_exit()
 
    def create_menu(self):
        self.menu = QMenu()
        


    def add_directory(self, label):
        qtIconFolder = QIcon(QApplication.style().standardIcon(QStyle.SP_DirIcon))        
        qtIconFile = QIcon(QApplication.style().standardIcon(QStyle.SP_FileIcon))  
        
        dirMenu = self.menu.addMenu(qtIconFolder, label)  
        # dirMenu.aboutToShow.connect(self.current_hover(dirMenu))
        dirMenu.aboutToShow.connect(lambda dirMenu=dirMenu : self.current_hover(dirMenu))

    def current_hover(self, item):
        print(item)

    def add_exit(self):
        qtIcon = QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
        exit = self.menu.addAction(qtIcon,'&Quit')      
        self.menu.insertSeparator(exit)
        exit.triggered.connect(self.exit_app)
        self.menu.exec_(QCursor.pos())

    def exit_app(self):
        self.close()
        sys.exit(0)
 
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)
