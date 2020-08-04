import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MenuItem Demo")
        self.set_size_request(400, 300)
        grid = Gtk.Grid()
        self.add(grid)

        menubar = Gtk.MenuBar()
        menubar.set_hexpand(True)
        grid.attach(menubar, 0, 0, 1, 1)

        menuitem_file = Gtk.MenuItem(label="File")
        menubar.append(menuitem_file)
        submenu_file = Gtk.Menu()
        menuitem_file.set_submenu(submenu_file)
        menuitem_open = Gtk.MenuItem(label="Open")
        submenu_file.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)

        menuitem_quit = Gtk.MenuItem(label="Quit")
        submenu_file.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)

        menuitem_edit = Gtk.MenuItem(label="Edit")
        menubar.append(menuitem_edit)

    def on_menu_open(self, widget):
        print("add file open dialog")

    def on_menu_quit(self, widget):
        Gtk.main_quit()


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()