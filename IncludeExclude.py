# This is a Data Class, that holds information about what:
# filenames, file-extensions, paths
# that will be included / excluded in the Menus.
from pathlib import Path

class IncludeExclude:
    def __init__(self):
        self.includePaths = []
        self.excludePaths = []
        self.includeFilenames = []
        self.includeExtensions = []
        self.excludeFilenames = []    
        self.excludeExtensions = []

    def folderIsNotExcluded(self, path: Path):

        # Full/path/with/forward/slashes
        fullpath = path.as_posix()
        includePaths = self.includePaths
        excludePaths = self.excludePaths

        willPass = False
        if len(includePaths) + len(excludePaths) == 0:
            return True

        if len(excludePaths) > 0:
            for str in excludePaths:
                if str in fullpath:
                    return False

        if len(includePaths) > 0:
            includePass = False
            for str in includePaths:
                if str in fullpath and includePass == False:
                    willPass = True
                    includePass = True
        else:
             willPass = True
                
        return willPass

    def fileIsNotExcluded(self, path: Path):
        
    
        filename = path.stem
        ext = path.suffix

        includeFilenames = self.includeFilenames
        includeExtensions = self.includeExtensions
        excludeFilenames = self.excludeFilenames
        excludeExtensions = self.excludeExtensions

        willPass = True

        # If no rules is present, it will pass
        if len(includeFilenames) + len(includeExtensions) + len(excludeFilenames) + len(excludeExtensions) == 0:
            return True
        
        # Exclude filenames
        if len(excludeFilenames) > 0:
            for str in excludeFilenames:
                if str in filename:
                    return False

        # Exclude extensions
        if len(excludeExtensions) > 0:
            for str in excludeExtensions:
                if str in ext:
                    return False
        
        # Include filenames
        if len(includeFilenames) > 0:
            for str in includeFilenames:
                if str in filename:
                    return True

        # Include extensions
        if len(includeExtensions) > 0:
            willPass = False
            for str in includeExtensions:
                if str in ext:
                    willPass = True

        return willPass