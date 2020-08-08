#!/usr/bin/python

# simple.py
from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QStyle
import sys
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
        QStyle.SP_ArrowBack,
        QStyle.SP_ArrowDown,
        QStyle.SP_ArrowForward,
        QStyle.SP_ArrowLeft,
        QStyle.SP_ArrowRight,
        QStyle.SP_ArrowUp,
        QStyle.SP_BrowserReload,
        QStyle.SP_BrowserStop,
        QStyle.SP_CommandLink,
        QStyle.SP_ComputerIcon,
        QStyle.SP_CustomBase,
        QStyle.SP_DesktopIcon,
        QStyle.SP_DialogAbortButton,
        QStyle.SP_DialogApplyButton,
        QStyle.SP_DialogCancelButton,
        QStyle.SP_DialogCloseButton,
        QStyle.SP_DialogDiscardButton,
        QStyle.SP_DialogHelpButton,
        QStyle.SP_DialogIgnoreButton,
        QStyle.SP_DialogNoButton,
        QStyle.SP_DialogNoToAllButton,
        QStyle.SP_DialogOkButton,
        QStyle.SP_DialogOpenButton,
        QStyle.SP_DialogResetButton,
        QStyle.SP_DialogRetryButton,
        QStyle.SP_DialogSaveAllButton,
        QStyle.SP_DialogSaveButton,
        QStyle.SP_DialogYesButton,
        QStyle.SP_DialogYesToAllButton,
        QStyle.SP_DirClosedIcon,
        QStyle.SP_DirHomeIcon,
        QStyle.SP_DirIcon,
        QStyle.SP_DirLinkIcon,
        QStyle.SP_DirLinkOpenIcon,
        QStyle.SP_DirOpenIcon,
        QStyle.SP_DockWidgetCloseButton,
        QStyle.SP_DriveCDIcon,
        QStyle.SP_DriveDVDIcon,
        QStyle.SP_DriveFDIcon,
        QStyle.SP_DriveHDIcon,
        QStyle.SP_DriveNetIcon,
        QStyle.SP_FileDialogBack,
        QStyle.SP_FileDialogContentsView,
        QStyle.SP_FileDialogDetailedView,
        QStyle.SP_FileDialogEnd,
        QStyle.SP_FileDialogInfoView,
        QStyle.SP_FileDialogListView,
        QStyle.SP_FileDialogNewFolder,
        QStyle.SP_FileDialogStart,
        QStyle.SP_FileDialogToParent,
        QStyle.SP_FileIcon,
        QStyle.SP_FileLinkIcon,
        QStyle.SP_LineEditClearButton,
        QStyle.SP_MediaPause,
        QStyle.SP_MediaPlay,
        QStyle.SP_MediaSeekBackward,
        QStyle.SP_MediaSeekForward,
        QStyle.SP_MediaSkipBackward,
        QStyle.SP_MediaSkipForward,
        QStyle.SP_MediaStop,
        QStyle.SP_MediaVolume,
        QStyle.SP_MediaVolumeMuted,
        QStyle.SP_MessageBoxCritical,
        QStyle.SP_MessageBoxInformation,
        QStyle.SP_MessageBoxQuestion,
        QStyle.SP_MessageBoxWarning,
        QStyle.SP_RestoreDefaultsButton,
        QStyle.SP_TitleBarCloseButton,
        QStyle.SP_TitleBarContextHelpButton,
        QStyle.SP_TitleBarMaxButton,
        QStyle.SP_TitleBarMenuButton,
        QStyle.SP_TitleBarMinButton,
        QStyle.SP_TitleBarNormalButton,
        QStyle.SP_TitleBarShadeButton,
        QStyle.SP_TitleBarUnshadeButton,
        QStyle.SP_ToolBarHorizontalExtensionButton,
        QStyle.SP_ToolBarVerticalExtensionButton,
        QStyle.SP_TrashIcon,
        QStyle.SP_VistaShield
        ]
        
        for item in icons:
            
            qtIcon = QIcon(QApplication.style().standardIcon(item))
            iconName = item.__str__()
            iconName2 = iconName.split('.')
            iconName3 = iconName2[-1] 
            
            myAction = QAction(qtIcon, iconName3, self)        
            fileMenu.addAction(myAction)

    def exit_app(self):
        self.close()
 
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)

