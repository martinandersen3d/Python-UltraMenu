# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

from Ui import FolderItem, FileItem
import sys
import os
from pathlib import Path
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
        super().__init__()
        
        self.objectList = {}
        self.icon = {
            'folder': QIcon(QApplication.style().standardIcon(QStyle.SP_DirIcon)),
            'file': QIcon(QApplication.style().standardIcon(QStyle.SP_FileIcon)),
            'quit': QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
        }
        
        self.create_menu()
        self.add_directory('&Scripts', '/SettingsMartin/Scripts')
        self.add_exit()
 
    def create_menu(self):
        self.menu = QMenu()
        self.menu.addAction('Add')

    def add_directory(self, label, dir):
        dirMenu = self.menu.addMenu(self.icon['folder'], label)
        
        list = self.get_directory(dir, dirMenu)
        for item in list:
            if type(item) is FolderItem:
                dirMenu.addMenu(self.icon['folder'], item.label)
            if type(item) is FileItem:
                dirMenu.addMenu(self.icon['file'], item.label)
               
            
    

    def get_directory(self, dir: str, parentMenu: QMenu):
        dirPath = dir
        filesAndFolders = sorted(Path(dirPath).glob('*'))
        filesAndFolders.sort(key=lambda x: x.is_file())
        filesAndFoldersArr = []

        for item in filesAndFolders:
            path = dirPath + '/' + item.name 
            if item.is_dir():
                folderItem = FolderItem(parentMenu, item.name, '', '', item, '')
                uid = folderItem.getUid()
                self.objectList[uid] = folderItem
                filesAndFoldersArr.append(folderItem)
            elif item.is_file():
                fileItem = FileItem(parentMenu, item.name, '', '', item, '')
                uid = folderItem.getUid()
                self.objectList[uid] = folderItem
                filesAndFoldersArr.append(fileItem)
                # filename
                # item.name
                # extension
                # item.suffix
            else:  
                print("It is a special file (socket, FIFO, device file)" )
        return filesAndFoldersArr
            

    def add_exit(self):
        exit = self.menu.addAction(self.icon['quit'],'&Quit')      
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