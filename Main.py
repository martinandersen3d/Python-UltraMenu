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
        self.add_directory('&Scripts', '/')
        self.add_exit()
 
    def create_menu(self):
        self.menu = QMenu()
        self.menu.addAction('Add')

    def add_directory(self, label, dir):
        qtParentMenuItem = self.menu.addMenu(self.icon['folder'], label)
        parentMenuClass = FolderItem(qtMenuItem = qtParentMenuItem, label = label, iconPath = '', globalHotkey = '', path = Path(dir))
        uid = parentMenuClass.getUid()
        self.objectList[uid] = parentMenuClass
        self.add_directory_submenu(parentMenuClass)

    def add_directory_submenu( self, parentMenuClass: FolderItem ):
        
        qtParentMenuItem = parentMenuClass.getQtMenuItem()
        
        if parentMenuClass.isSubmenuItemsAdded == False:
            parentMenuClass.isSubmenuItemsAdded = True
            dirPath: str = parentMenuClass.getFullPath()
            osPaths = sorted(Path(dirPath).glob('*'))
            osPaths.sort(key=lambda x: x.is_file())
            filesAndFoldersArr = []

            for item in osPaths:
                # path = dirPath + '/' + item.name 
                if item.is_dir():
                    qtFolderItem = qtParentMenuItem.addMenu( self.icon['folder'], '&' + item.name)
                    folderItemClass = FolderItem(qtMenuItem = qtFolderItem, label = item.name, iconPath = '', globalHotkey = '', path = item)
                    uid = folderItemClass.getUid()
                    self.objectList[uid] = folderItemClass
                    filesAndFoldersArr.append(folderItemClass)
                    qtFolderItem.aboutToShow.connect(lambda folderItemClass=folderItemClass : self.add_directory_submenu(folderItemClass))
                    # newFolder.triggered.connect(self.action_directory(item.uid))
                    
                elif item.is_file():
                    qtFileItem = qtParentMenuItem.addAction(self.icon['file'], item.name)
                    folderItemClass = FolderItem(qtMenuItem = qtFileItem, label = item.name, iconPath = '', globalHotkey = '', path = item)
                    uid = folderItemClass.getUid()
                    self.objectList[uid] = folderItemClass
                    filesAndFoldersArr.append(folderItemClass)
                    # filename
                    # item.name
                    # extension
                    # item.suffix
                    # newFile.triggered.connect(self.action_directory(item.uid))
                    #         # newFile.hovered.connect(self.exit_app)
                    #         # newFile.hovered.connect(lambda:  item.printUid())

                    #         # func = self.hover()
                    #         # newFile.hovered.connect(lambda f=func,arg=newFile:f(arg))
                else:  
                    print("It is a special file (socket, FIFO, device file)" )
            
    def action_directory(self, uid):
        print(uid)         

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