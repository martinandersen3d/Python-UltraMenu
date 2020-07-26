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
from tkinter import * #ttk, PhotoImage, Label, Menu, Frame, Button
from tkinter import ttk #ttk, PhotoImage, Label, Menu, Frame, Button
from PIL import Image
from ttkthemes import ThemedTk
import tkinter.font as tkFont

script_dir = os.path.dirname(os.path.abspath(__file__))
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        themeBg = self.from_rgb((60,63,65))
        themeFg = self.from_rgb((187,187,187))
        themeActiveBg = self.from_rgb((75,110,175))
        themeActiveFg = self.from_rgb((200,200,200))
        # relief (menu border) : must be flat, groove, raised, ridge, solid, or sunken
        themeRelief = 'flat'
        
        # default_font = tkFont.nametofont("TkDefaultFont")
        custom_font = tkFont.Font(family="Helvetica", size=9)
        
        self.master.title("Submenu")

        # https://www.javatpoint.com/python-tkinter-menu
        # 	postcommand	The postcommand can be set to any of the function which is called when the mourse hovers the menu.
        menubar = Menu(self.master, tearoff=False)
        self.master.config(menu=menubar)

        
        fileMenu = Menu(menubar, tearoff=False,  
                        background=themeBg , foreground=themeFg,
                       activebackground=themeActiveBg, activeforeground=themeActiveFg, font=custom_font,
                       activeborderwidth=0,
                        relief=themeRelief
                       )
        fileMenu.config(bg = themeBg) 

        # image = Image.open(os.path.join(script_dir, 'fleur.jpg'))
        photo = PhotoImage(file=r'image3.png')
        label2 = ttk.Label(image=photo)
        label2.image = photo # keep a reference!
        # label2.pack()

        submenu = Menu(fileMenu, tearoff=False,  title="sdfsdfsdf",
                        background=themeBg , foreground=themeFg,
                       activebackground=themeActiveBg, activeforeground=themeActiveFg, font=custom_font,
                       activeborderwidth=0,
                        relief=themeRelief
                       )
        fileMenu.config(bg = themeBg) 
        submenu.add_command(label='First Page            ', underline=0, accelerator='                      Home')
        # submenu.add_command(label="Bookmarks", image=photo,compound=LEFT)
        submenu.add_command(label="   Bookmarks", image=photo,compound=LEFT, underline=3)
        submenu.add_command(label="Bookmarks", image=photo,compound=LEFT, underline=0)
        submenu.add_command(label="Bookmarks", image=photo,compound=LEFT, underline=0)
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

    def from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb 
    
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

    # root = Tk()
    root = ThemedTk(theme="clearlooks")
    
    # root = Tk()
    # root.style = Style()
    # #('clam', 'alt', 'default', 'classic')
    # root.style.theme_use("clam")
    
    root.geometry("250x150+2900+300")
    button=ttk.Button(root,text="Click Me", underline=6)
    button.pack()
    root.configure(bg='red')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
    

