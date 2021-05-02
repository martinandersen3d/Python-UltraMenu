#!/usr/bin/python

# simple.py
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QStyle
import sys
from pathlib import Path
from PySide2.QtGui import QIcon
# cross platform copy/paste
# pip3 install pyperclip
import pyperclip
# 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Simple Note Pad Application")
        self.setGeometry(2500,300,500,400)
 
        self.create_menu()
 
        self.show()
 
    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&All Icons")
        
        icons = [
        
        ]
        
        osPaths = Path('./icons/filetypes_flat').glob('*.png')
        print(str(osPaths))
        for item in osPaths:
            filename = item.name + '.' + item.suffix
            qtIcon = QIcon(str(item))
            iconName = item.name

            
            myAction = QAction(qtIcon, iconName, self)        
            fileMenu.addAction(myAction)

    def exit_app(self):
        self.close()
 
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)

