import uuid 
from PySide2.QtWidgets import  QAction, QMenu
from pathlib import Path
import IncludeExclude
# dictionary = {'key1': 'val1', '1': 'val2'}

class BaseItem:
    def __init__(self,  qtMenuItem: QMenu, label: str):
        # Set a random string as the uid for the object
        self.uid = uuid.uuid4().hex
        self.label = label
        # self.parentMenuClass = parentMenuClass
        self.qtMenuItem = qtMenuItem
        
        # Include / Exclude -------------------------------
        self.includeExclude: IncludeExclude = None
        
    # Todo: add uid to global dictionary
    
    # Add Child
    def add(self):
        return True
    
    # Get Children
    def getChildren(self):
        return True
    
    # Get Children
    def getUid(self):
        return self.uid
    
    
    # Get qtMenuItem
    def getQtMenuItem(self):
        return self.qtMenuItem
    
    
    # Set IncludeExlude files, ext's, paths
    def setExcludeInclude(self, includeExclude: IncludeExclude):
        self.includeExclude = includeExclude
    
    
    # Remove this object
    def removeSelf(self):
        return True
    
class MenuItem(BaseItem):
    def __init__(self, qtMenuItem: QMenu,  label: str, iconPath:str, globalHotkey:str):
        super().__init__( qtMenuItem, label)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
    
class SubMenuItem(BaseItem):
    def __init__(self, qtMenuItem: QMenu, label: str, iconPath:str, globalHotkey:str):
        super().__init__( qtMenuItem, label)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey

class SeperatorItem(BaseItem):
    def __init__(self,  qtMenuItem: QMenu,  label: str):
        super().__init__( qtMenuItem, label)

class FolderItem(BaseItem):
    def __init__(self, qtMenuItem: QMenu, label: str, iconPath:str, globalHotkey:str, path: Path):
        super().__init__(qtMenuItem,  label)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
        self.osPath = path
        self.isSubmenuItemsAdded = False
        
    def getFullPath(self):
        # return ''
        return str(self.osPath)
        # return self.osPath._str
        
    def printUid(self):
        print(self.uid)


        
class FileItem(BaseItem):
    def __init__(self, qtMenuItem: QMenu, label: str, iconPath:str, globalHotkey:str, path: Path):
        super().__init__(qtMenuItem,  label)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
        self.osPath = path

    def getFullPath(self):
        return str(self.osPath)
        
    def onClick(self):
        self.getFullPath()
        
    def printUid(self):
        print(self.uid)

