# https://pypi.org/project/natsort/
# sudo pip3 install natsort

import os
from pathlib import Path

dirPath = '/home/m'

filesAndFolders = sorted(Path(dirPath).glob('*'))
filesAndFolders.sort(key=lambda x: x.is_file())
# filesAndFolders.filt

for item in filesAndFolders:
    path = dirPath + '/' + item.name 
    if item.is_dir():
        # filename
        item.name
    elif item.is_file():
        # filename
        item.name
        # extension
        item.suffix
    else:  
        print("It is a special file (socket, FIFO, device file)" )

