# https://pypi.org/project/natsort/
# sudo pip3 install natsort

import os
from pathlib import Path

dirPath = '/home/m'
unsortedFilesAndFolders = os.listdir(dirPath)
unsortedFolders = []
unsortedFiles = []
sortedFolders = sorted(unsortedFolders)
sortedFiles = sorted(unsortedFiles)

for item in unsortedFilesAndFolders:
    # print(item)
    path = dirPath + '/' + item 
    pathObj = Path(path)
    if pathObj.is_dir():
        unsortedFolders.append(item)
    elif pathObj.is_file():
        unsortedFiles.append(item)
        # return: '.zip' or on a '/.bash' it will return ''
        # print(Path(path).filename)
        print(item + '___' +Path(path).suffix)
    else:  
        print("It is a special file (socket, FIFO, device file)" )

