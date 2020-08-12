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
# Intellisence works best, when imported this way
from IncludeExclude import IncludeExclude
# from PySide.QtGui import *
# from PySide.QtCore import *
# cross platform copy/paste
# pip3 install pyperclip
# import pyperclip
# 

bgColor='#1F1F1F'
appStyle="""
QMenu QAbstractItemView  {{ border: 0px solid black; background-color: rgb(60,63,65); color: rgb(187,187,187); border-radius: 0; }}
QMenu {{ font-family:Helvetica; font-size:13px; selection-background-color: #ffaa00; selection-color: black; background-color: rgb(60,63,65); border-style: solid; border: 0px solid #EBEBEB; border-radius: 0; color: rgb(187,187,187); padding: 0px 0px 0px 0px; }}
QMenu:on  {{padding-top: 0px; padding-left: 0px; background-color: #AAAAAA; selection-background-color: #ffaa00; color: #EBEBEB; border-radius: 0;}}
QMenu:item:selected {{ border: 0px solid #ffa02f; background-color: rgb(75,110,175); color: rgb(222,222,222);}}
QMenu::item {{padding: 4px 20px 4px 12px; }}
QMenu::icon {{padding-left: 11px; }}
""".format(bgColor) 

# family="Helvetica", size=9
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        # Config --------------------------------------
        self.objectList = {}
        self.systemIcon = {
            'folder': QIcon(QApplication.style().standardIcon(QStyle.SP_DirIcon)),
            'folderLink': QIcon(QApplication.style().standardIcon(QStyle.SP_DirLinkIcon)),
            'file': QIcon(QApplication.style().standardIcon(QStyle.SP_FileIcon)),
            'quit': QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
        }
        self.filetypeIcon= Icons.icon_filetypes_flat(self)
        self.includeExclude = IncludeExclude()
        self.includeExclude.includePaths = ['Examples', 'py', 'png']
        self.includeExclude.includeExtensions = ['md', 'py', 'png']
        self.includeExclude.excludeFilenames = ['gitignore']
        self.includeExclude.excludePaths = ['git', '__pycache__']
        
        
        # --------------------------------------------
        self.create_menu()
        self.add_directory('&Scripts', '/media/m/Data/Development/Phyton/TreeViewUltraMenu/Python-UltraMenu')
        self.add_exit()
 
    def create_menu(self):
        self.menu = QMenu(self)
        # Enable theme, uncomment:
        self.menu.setStyleSheet(appStyle)
        self.menu.setCursor(QtCore.Qt.PointingHandCursor) 
        self.menu.addAction('Add')

    def add_directory(self, label, dir):
        
        qtParentMenuItem = self.menu.addMenu(self.systemIcon['folder'], label)
        parentMenuClass = FolderItem(qtMenuItem = qtParentMenuItem, label = label, iconPath = '', globalHotkey = '', path = Path(dir))
        uid = parentMenuClass.getUid()
        self.objectList[uid] = parentMenuClass
        self.add_directory_submenu(parentMenuClass)

    def add_directory_submenu( self, parentMenuClass: FolderItem ):

        qtParentMenuItem = parentMenuClass.getQtMenuItem()
        
        # Don't add the menu items multiple times, every time you hover a submenu.
        if parentMenuClass.isSubmenuItemsAdded == True:
            return None
        
        parentMenuClass.isSubmenuItemsAdded = True
        dirPath: str = parentMenuClass.getFullPath()
        osPaths = sorted(Path(dirPath).glob('*'))
        osPaths.sort(key=lambda x: x.is_file())
        filesAndFoldersArr = []

        for item in osPaths:
            # path = dirPath + '/' + item.name 
            if item.is_dir() == True and self.includeExclude.folderIsNotExcluded(item):
                
                folderIcon = self.systemIcon['folder']
                
                if item.is_symlink():
                    folderIcon = self.systemIcon['folderLink']
                    
                qtFolderItem = qtParentMenuItem.addMenu( folderIcon, '&' + item.name)
                folderItemClass = FolderItem(qtMenuItem = qtFolderItem, label = item.name, iconPath = '', globalHotkey = '', path = item)
                uid = folderItemClass.getUid()
                self.objectList[uid] = folderItemClass
                filesAndFoldersArr.append(folderItemClass)
                qtFolderItem.aboutToShow.connect(lambda folderItemClass=folderItemClass : self.add_directory_submenu(folderItemClass))
                    # newFolder.triggered.connect(self.action_directory(item.uid))
                
            elif item.is_file() and self.includeExclude.fileIsNotExcluded(item):
                
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