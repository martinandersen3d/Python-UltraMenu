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
        qtParentMenuItem = self.menu.addMenu(self.icon['folder'], label)
        parentMenuClass = FolderItem(qtMenuItem = qtParentMenuItem, label = label, iconPath = '', globalHotkey = '', path = Path(dir))
        uid = parentMenuClass.getUid()
        self.objectList[uid] = parentMenuClass
        self.add_directory_submenu(parentMenuClass)

    def add_directory_submenu( self, parentMenuClass: FolderItem ):
        
        qtParentMenuItem = parentMenuClass.getQtMenuItem()
        
        dirPath = parentMenuClass.getFullPath()
        filesAndFolders = sorted(Path(dirPath).glob('*'))
        filesAndFolders.sort(key=lambda x: x.is_file())
        filesAndFoldersArr = []

        for item in filesAndFolders:
            # path = dirPath + '/' + item.name 
            if item.is_dir():
                qtFolderItem = qtParentMenuItem.addMenu( self.icon['folder'], '&' + item.name)
                folderItemClass = FolderItem(qtMenuItem = qtFolderItem, label = item.name, iconPath = '', globalHotkey = '', path = item)
                uid = folderItemClass.getUid()
                self.objectList[uid] = folderItemClass
                filesAndFoldersArr.append(folderItemClass)
                qtFolderItem.aboutToShow.connect(lambda folderItemClass=folderItemClass : self.add_directory_submenu(folderItemClass))
                
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
            else:  
                print("It is a special file (socket, FIFO, device file)" )
        
        
        
        # list = self.get_directory(parentMenuClass)
        # for item in list:
        #     if type(item) is FolderItem:
                

        #         # dirMenu.setMouseTracking(True)
        #         # dirMenu.mouseMoveEvent(print('sdf'))
        #         # newFolder.mouseMoveEvent(self.hover(QMouseEvent ))
        #         # newFolder.aboutToShow(self.action_directory(item.uid))
        #         # newFolder.triggered.connect(self.action_directory(item.uid))
                
        #         # newFolder.aboutToShow.connect(lambda:  item.printUid())
        #         # newFolder.aboutToShow.connect(self.action_directory(item.uid))
        #         newFolder.aboutToShow.connect(lambda item=item : self.hover(item))
                
        #     if type(item) is FileItem:
                
        #         newFile = qtParentMenuItem.addAction(self.icon['file'], item.label)
        #         # newFile.triggered.connect(self.action_directory(item.uid))
        #         # newFile.hovered.connect(self.exit_app)
        #         # newFile.hovered.connect(lambda:  item.printUid())
                
        #         # func = self.hover()
        #         # newFile.hovered.connect(lambda f=func,arg=newFile:f(arg))
                

    # def get_directory(self, parentMenuClass: FolderItem):
    #     dirPath = parentMenuClass.getFullPath()
    #     filesAndFolders = sorted(Path(dirPath).glob('*'))
    #     filesAndFolders.sort(key=lambda x: x.is_file())
    #     filesAndFoldersArr = []

    #     for item in filesAndFolders:
    #         # path = dirPath + '/' + item.name 
    #         if item.is_dir():
    #             folderItem = FolderItem(parentMenuClass, item.name, '', '', item, '')
    #             uid = folderItem.getUid()
    #             self.objectList[uid] = folderItem
    #             filesAndFoldersArr.append(folderItem)
    #         elif item.is_file():
    #             fileItem = FileItem(parentMenuClass, item.name, '', '', item, '')
    #             uid = fileItem.getUid()
    #             self.objectList[uid] = fileItem
    #             filesAndFoldersArr.append(fileItem)
    #             # filename
    #             # item.name
    #             # extension
    #             # item.suffix
    #         else:  
    #             print("It is a special file (socket, FIFO, device file)" )
    #     return filesAndFoldersArr

    def action_directory(self, uid):
        print(uid)

    def hover(self, args ) -> None:
        print(args.uid)
        # """Simulate a mouse hover over the element."""
        # pos = self._mouse_pos()
        # event = QMouseEvent(QEvent.MouseMove, pos, Qt.NoButton, Qt.NoButton,
        #                     Qt.NoModifier)
        # self._tab.send_event(event)             

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