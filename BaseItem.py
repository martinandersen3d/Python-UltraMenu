import uuid 

# dictionary = {'key1': 'val1', '1': 'val2'}

class BaseItem:
    def __init__(self, x, y, z):
        # Set a random string as the uid for the object
        self.uid = uuid.uuid4().hex
        self.iconPath = iconPath
        self.label = label
        self.globalHotkey = globalHotkey
        self.isSeperator = isSeparator
        self.x = x
        self.y = y
        self.z = z
    # Todo: add uid to global dictionary
    
    # Add Child
    def add(self):
        return True
    
    # Get Children
    def getChildren(self):
        return True
    
    
    # Remove this object
    def removeSelf(self):
        return True
    
    