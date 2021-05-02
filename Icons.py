from pathlib import Path

def icon_filetypes_flat(self) -> dict:
    
    osPaths = Path('./icons/filetypes_flat').glob('*.png')

    iconsDict = {}

    for osPath in osPaths:
        iconsDict.update( { '.' + osPath.stem : osPath} )
    
    return iconsDict
