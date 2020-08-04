#!/usr/bin/env python

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
        self.menu.show_all()
        
        # Seperator ---------------------------
        self.seperator = Gtk.SeparatorMenuItem()
        self.menu.append(self.seperator)
        
        # -------------------------------------
        # Show Application Window
        self.show_all()

    def on_window_loaded(self, widget, context):
        print('Loaded')
        self.menu.popup_at_pointer()

TransparentWindow()
Gtk.main()