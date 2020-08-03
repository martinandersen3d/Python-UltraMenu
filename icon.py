from PIL import Image

newIconColor = (255,0,0) 

img = Image.open('icon.png') 
img = img.convert("RGBA") 
background = Image.new('RGBA', (24, 24), (255, 255, 255,0))
background.paste(newIconColor, (0, 0),img)
background.save("new_icon.png", "PNG")



