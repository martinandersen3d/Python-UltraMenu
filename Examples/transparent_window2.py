#!/usr/bin/env python
# https://developer.gimp.org/api/2.0/gtk/GtkWindow.html#gtk-window-set-decorated
# https://stackoverflow.com/questions/29998606/in-gtk3-for-python-how-to-get-selected-menuitem-or-index-of-menuitem-selected
# https://lazka.github.io/pgi-docs/Gtk-3.0/classes.html

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

class TransparentWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_size_request(300, 220)

        self.connect('destroy', Gtk.main_quit)
        # draw is when the GUI is fully loaded.
        self.connect('draw', self.on_window_loaded)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        
        # Show / Hide: Titlebar, minimize, maximize, close
        self.set_decorated(False)
        
        # Show / Hide: Application body
        self.set_app_paintable(True)
        
        # Add Simple Menu item ---------------------------
        self.menu = Gtk.Menu.new()
        self.menuItem = Gtk.MenuItem.new_with_mnemonic('_Something')
        self.menu.append(self.menuItem)
        
        # Seperator ---------------------------
        self.seperator = Gtk.SeparatorMenuItem()
        self.menu.append(self.seperator)
        
        # Menu Item Quit -----------------------
        self.menuItemQuit = Gtk.MenuItem.new_with_mnemonic('_Quit')
        # self.menuItemQuit.add_action(Gtk.main_quit)
        self.menu.append(self.menuItemQuit)
        
        # menuItem.select()
        # self.menu.item_select(menuItem)
        
        # Show Popup Menu
        self.menu.show_all()

        # -------------------------------------
        # Show Application Window
        self.show_all()

    def on_window_loaded(self, widget, context):
        print('Window Gui is Loaded')
        self.menu.popup_at_pointer()
        self.menuItem.select()
        self.menuItem.set_use_underline(True)
        

TransparentWindow()
Gtk.main()