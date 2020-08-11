# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

import sys
import os
from pathlib import Path
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QStyle, QAction, QMenu
from PySide2.QtGui import QIcon, QCursor
import PySide2.QtCore  as QtCore
from PySide2 import QtGui, QtCore
# -------------------------------
from Ui import FolderItem, FileItem
import Icons


# from PySide.QtGui import *
# from PySide.QtCore import *
# cross platform copy/paste
# pip3 install pyperclip
# import pyperclip
# 

bgColor='#1F1F1F'
appStyle="""
QToolButton {{border: 0px solid #0F0F0F; background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #7A7A7A, stop: 1 #0F0F0F); color: #EBEBEB}}
QMenu QAbstractItemView  {{ border: 0px solid black; background-color: #7A7A7A; color: #EBEBEB; border-radius: 0; }}
QMenu {{  font-size:10pt; selection-background-color: #ffaa00; selection-color: black; background-color: #7A7A7A; border-style: solid; border: 0px solid #EBEBEB; border-radius: 0; color: #EBEBEB; padding: 0px 0px 0px 0px; }}
QMenu:on  {{padding-top: 0px; padding-left: 0px; background-color: #7A7A7A; selection-background-color: #ffaa00; color: #EBEBEB; border-radius: 0;}}
QMenu:hover {{ border: 0px solid #ffa02f; }}
QMenu::item {{padding-left: 20px; }}
QMenu::drop-down  {{ border-radius: 0px; background-color: #7A7A7A; color: #EBEBEB; }}""".format(bgColor) 


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.objectList = {}
        self.systemIcon = {
            'folder': QIcon(QApplication.style().standardIcon(QStyle.SP_DirIcon)),
            'file': QIcon(QApplication.style().standardIcon(QStyle.SP_FileIcon)),
            'quit': QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
        }
        self.filetypeIcon= Icons.icon_filetypes_flat(self)
        
        self.create_menu()
        self.add_directory('&Scripts', '/home/m/Downloads')
        self.add_exit()
 
    def create_menu(self):
        self.menu = QMenu(self)
        # self.menu.setStyleSheet("QMenu {padding-left: 50px; padding-right: 20px;}")
        # self.menu.setStyleSheet("QMenu::icon {padding-left: 50px; padding-right: 20px;}")
        self.menu.setStyleSheet(appStyle)
        self.menu.addAction('Add')

    def add_directory(self, label, dir):
        qtParentMenuItem = self.menu.addMenu(self.systemIcon['folder'], label)
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
                    qtFolderItem = qtParentMenuItem.addMenu( self.systemIcon['folder'], '&' + item.name)
                    folderItemClass = FolderItem(qtMenuItem = qtFolderItem, label = item.name, iconPath = '', globalHotkey = '', path = item)
                    uid = folderItemClass.getUid()
                    self.objectList[uid] = folderItemClass
                    filesAndFoldersArr.append(folderItemClass)
                    qtFolderItem.aboutToShow.connect(lambda folderItemClass=folderItemClass : self.add_directory_submenu(folderItemClass))
                    # newFolder.triggered.connect(self.action_directory(item.uid))
                    
                elif item.is_file():
                    
                    fileExt = item.suffix
                    
                    qtIcon = self.systemIcon['file']
                    
                    # If we have a icon for the filetype, use that instead
                    if fileExt in self.filetypeIcon:
                        qtIcon = QIcon(str(self.filetypeIcon[fileExt]))
                        
                    qtFileItem = qtParentMenuItem.addAction(qtIcon, item.name)
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
        exit = self.menu.addAction(self.systemIcon['quit'],'&Quit')      
        self.menu.insertSeparator(exit)
        exit.triggered.connect(self.exit_app)
        self.menu.exec_(QCursor.pos())

    def exit_app(self):
        self.close()
        sys.exit(0)
 
 
myApp = QApplication(sys.argv)
window = Window()
window.setStyleSheet(appStyle)
myApp.exec_()
sys.exit(0)