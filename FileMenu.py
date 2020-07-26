# http://zetcode.com/tkinter/menustoolbars/
#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script we create a submenu
a separator and keyboard shortcuts to menus.

Author: Jan Bodnar
Website: www.zetcode.com
"""
import os.path
from tkinter import *
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Submenu")

        menubar = Menu(self.master, tearoff=False)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff=False)

        # image = Image.open(os.path.join(script_dir, 'fleur.jpg'))
        photo = PhotoImage(file=r'image.png')
        label2 = Label(image=photo)
        label2.image = photo # keep a reference!
        # label2.pack()

        submenu = Menu(fileMenu, tearoff=False)
        submenu.add_command(label='First Page', underline=0, accelerator='Home')
        submenu.add_command(label="Bookmarks", image=photo,compound=LEFT)
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)


        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)



        # self.menubar = Menu(menubar)

        # self.read_menu = Menu(self.master, tearoff=False)
        # self.menubar.add_cascade(label='Read', underline=0, menu=self.read_menu)
        # self.menubar.add_command(label='First Page', underline=0, accelerator='Home')
        # self.menubar.add_command(label='Last Page', underline=1, image=self.read_last_image, compound=LEFT, command=self.menu_read_last, accelerator='End')
        # self.menubar.add_command(label='Next Page', underline=0, image=self.read_next_image, compound=LEFT, command=self.menu_read_next, accelerator='PgDn')
        # self.menubar.add_command(label='Previous Page', underline=0, image=self.read_previous_image, compound=LEFT, command=self.menu_read_previous, accelerator='PgUp')

        # self.menubar.add_separator()
        # self.menubar.add_command(command=self.menu_read_first, image=self.read_first_image)
        # self.menubar.add_command(command=self.menu_read_previous, image=self.read_previous_image)
        # self.menubar.add_command(command=self.menu_read_next, image=self.read_next_image)
        # self.menubar.add_command(command=self.menu_read_last, image=self.read_last_image)

    def loadImage():
        # img = Image.open("fleur.jpg")
        # filename = PhotoImage(img)
        # canvas = Canvas(gui,height=100,width=100)
        # canvas.image = filename  # <--- keep reference of your image
        # canvas.create_image(0,0,anchor='nw',image=filename)
        # canvas.pack()
        image = Image.open("fleur.jpg")
        photo = PhotoImage(file=image)
        # label = Label(image=photo)
        # label.pack()

    def onExit(self):

        self.quit()


def main():

    root = Tk()
    root.geometry("250x150+2900+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()