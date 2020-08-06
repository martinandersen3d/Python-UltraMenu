# https://wiki.qt.io/Qt_for_Python
# https://wiki.qt.io/PySide_Downloads
# https://wiki.qt.io/PySide_Binaries_Linux
# https://wiki.qt.io/PySide_Binaries_Windows
# https://wiki.qt.io/PySide_Binaries_MacOSX
# https://doc.qt.io/qtforpython/gettingstarted.html
# License: https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5

from PySide2.QtWidgets import QApplication,QMainWindow, QAction
import sys
from PySide2.QtGui import QIcon
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Simple Note Pad Application")
        self.setGeometry(2500,300,500,400)
 
        self.create_menu()
 
        self.show()
 
 
    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        searchMenu = mainMenu.addMenu("Font")
        helpMenu = mainMenu.addMenu("Help")
 
        openAction = QAction(QIcon('./Examples/Icons/icon.png'), "Open", self)
        openAction.setShortcut("Ctrl+O")
 
        saveAction = QAction(QIcon('save.png'), "&Save", self)
        saveAction.setShortcut("s")

        save2Action = QAction(QIcon('save.png'), "&Save", self)
        save2Action.setShortcut("Ctrl+S")
 
        exitAction = QAction(QIcon('exit.png'), "&Exit", self)
        exitAction.setShortcut("Ctrl+X")
 
        exitAction.triggered.connect(self.exit_app)
 
 
 
        fileMenu.addAction(openAction)
        fileMenu.addMenu("addMenu")
        fileMenu.addAction(saveAction)
        fileMenu.addAction(save2Action)
        # seperator
        fileMenu.insertSeparator(save2Action)
        
        fileMenu.insertSection(saveAction, QIcon('./Examples/Icons/icon.png'), "Insert Section")
        fileMenu.addAction(exitAction)
 
 
    def exit_app(self):
        self.close()
 
 
 
 
 
 
 
 
 
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)