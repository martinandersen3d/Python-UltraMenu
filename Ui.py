import uuid 
from PySide2.QtWidgets import  QAction, QMenu
from pathlib import Path
# dictionary = {'key1': 'val1', '1': 'val2'}

class BaseItem:
    def __init__(self, parentMenu, label: str):
        # Set a random string as the uid for the object
        self.uid = uuid.uuid4().hex
        self.label = label
        self.parentMenu = parentMenu

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
    
    
    # Remove this object
    def removeSelf(self):
        return True
    
class MenuItem(BaseItem):
    def __init__(self, parentMenu, label: str, iconPath:str, globalHotkey:str):
        super().__init__(parentMenu, label, iconPath)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
    
class SubMenuItem(BaseItem):
    def __init__(self, parentMenu, label: str, iconPath:str, globalHotkey:str):
        super().__init__(parentMenu, label, iconPath)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey

class SeperatorItem(BaseItem):
    def __init__(self, parentMenu, label: str):
        super().__init__(parentMenu, label)

class FolderItem(BaseItem):
    def __init__(self, parentMenu, label: str, iconPath:str, globalHotkey:str, path: Path, action):
        super().__init__(parentMenu, label, iconPath)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
        self.path = path

class FileItem(BaseItem):
    def __init__(self, parentMenu, label: str, iconPath:str, globalHotkey:str, path: Path, action):
        super().__init__(parentMenu, label, iconPath)
        self.iconPath = iconPath
        self.globalHotkey = globalHotkey
        self.path = path
    