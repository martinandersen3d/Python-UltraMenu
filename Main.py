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
                newFolder = dirMenu.addMenu( self.icon['folder'], '&' + item.label)

                # dirMenu.setMouseTracking(True)
                # dirMenu.mouseMoveEvent(print('sdf'))
                # newFolder.mouseMoveEvent(self.hover(QMouseEvent ))
                # newFolder.aboutToShow(self.action_directory(item.uid))
                # newFolder.triggered.connect(self.action_directory(item.uid))
                
                # newFolder.aboutToShow.connect(lambda:  item.printUid())
                # newFolder.aboutToShow.connect(self.action_directory(item.uid))
                newFolder.aboutToShow.connect(lambda item=item : self.hover(item))
                
            if type(item) is FileItem:
                
                newFile = dirMenu.addAction(self.icon['file'], item.label)
                # newFile.triggered.connect(self.action_directory(item.uid))
                # newFile.hovered.connect(self.exit_app)
                # newFile.hovered.connect(lambda:  item.printUid())
                
                # func = self.hover()
                # newFile.hovered.connect(lambda f=func,arg=newFile:f(arg))
                
                

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
                uid = fileItem.getUid()
                self.objectList[uid] = fileItem
                filesAndFoldersArr.append(fileItem)
                # filename
                # item.name
                # extension
                # item.suffix
            else:  
                print("It is a special file (socket, FIFO, device file)" )
        return filesAndFoldersArr

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