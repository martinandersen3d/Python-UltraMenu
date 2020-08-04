# https://www.tutorialspoint.com/pygtk/pygtk_menubar_menu_menuitem.htm
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PyApp(Gtk.Window):
    def __init__(self):
      
        super(PyApp, self).__init__()
        self.set_title("Menu Demo")
        self.set_default_size(250, 200)
        # self.set_position(Gtk.WIN_POS_CENTER)

        mb = Gtk.MenuBar()

        menu1 = Gtk.Menu()
        file = Gtk.MenuItem("_File")
        file.set_submenu(menu1)
        acgroup = Gtk.AccelGroup()
        self.add_accel_group(acgroup)
        new = Gtk.ImageMenuItem(Gtk.STOCK_NEW,acgroup)
        # new.add_accelerator("activate", acgroup, ord('N'), 
        #     Gtk.gdk.CONTROL_MASK, Gtk.ACCEL_VISIBLE)

        menu1.append(new)
        open = Gtk.ImageMenuItem(Gtk.STOCK_OPEN)

        menu1.append(open)
        chk = Gtk.CheckMenuItem("Checkable")

        menu1.append(chk)
        radio1 = Gtk.RadioMenuItem(None,"Radio1")
        radio2 = Gtk.RadioMenuItem(radio1, "Radio2")

        menu1.append(radio1)
        menu1.append(radio2)
        sep = Gtk.SeparatorMenuItem()

        menu1.append(sep)
        exit = Gtk.ImageMenuItem(Gtk.STOCK_QUIT)

        menu1.append(exit)
        menu2 = Gtk.Menu()
        edit = Gtk.MenuItem("_Edit")
        edit.set_submenu(menu2)
        copy = Gtk.ImageMenuItem(Gtk.STOCK_COPY)

        menu2.append(copy)
        cut = Gtk.ImageMenuItem(Gtk.STOCK_CUT)

        menu2.append(cut)
        paste = Gtk.ImageMenuItem(Gtk.STOCK_PASTE)

        menu2.append(paste)
        mb.append(file)
        mb.append(edit)
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
      
if __name__ == '__main__':
    PyApp()
    Gtk.main()