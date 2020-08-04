#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/54847454/right-click-context-menu-with-pygobject
# http://zetcode.com/gui/gtksharp/menus/
# Acc-group: https://athenajc.gitbooks.io/python-gtk-3-api/content/gtk-group/gtkmenuitem.html
# Item:     https://www.tutorialspoint.com/pygtk/pygtk_menubar_menu_menuitem.htm
# Submenu:  https://stackoverflow.com/questions/52847909/how-to-add-a-sub-menu-to-a-gtk-menu
# Image:    https://stackoverflow.com/questions/4318943/how-can-a-custom-icon-be-used-in-an-image-menu-item
# The following are some of the predefined modifiers −

# SHIFT_MASK
# LOCK_MASK
# CONTROL_MASK
# BUTTON1_MASK
# BUTTON1_MASK

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.resize(100, 100)

        self._build_context_menu()

        # button event
        self.connect('button-press-event', self._on_button_press_event)

        # close event
        self.connect('delete-event', self._on_delete_event)

    def _build_context_menu(self):

        # Add Simple Menu item ---------------------------
        self.cmenu = Gtk.Menu.new()
        # self.cm_item = Gtk.MenuItem.new_with_label('label')
        self.cm_item = Gtk.MenuItem.new_with_mnemonic('_Lab_el')
        self.cmenu.append(self.cm_item)
        
        # Add Seperator ---------------------------
        self.seperator = Gtk.SeparatorMenuItem()
        self.cmenu.append(self.seperator)
        
        
        # Add Simple Menu item + Hotkey group-----------------------------
        accelgroup = Gtk.AccelGroup()
        self.add_accel_group(accelgroup) 
        # -----------------------------
        # self.menuitem_open = Gtk.MenuItem(label="Open")      
        self.menuitem_open = Gtk.MenuItem.new_with_mnemonic('_Open')     
        self.menuitem_open.connect('activate', self.on_menu_open)
        self.menuitem_open.add_accelerator("activate", 
                                accelgroup,
                                Gdk.keyval_from_name("o"),
                                Gdk.ModifierType.CONTROL_MASK,
                                Gtk.AccelFlags.VISIBLE)
        self.cmenu.append(self.menuitem_open)
        
        
        # Submenu-----------------------------
        # self.submenu = Gtk.Menu.new()
        # self.submenu_item = Gtk.MenuItem.new_with_mnemonic('L_abel2')
        # self.cmenu.append(self.submenu_item)
        #  Menu can only be attached to a MenuItem and a MenuItem can only be added to a Menu or a Menubar.

        item = Gtk.MenuItem.new_with_mnemonic('_1 Submenu') 
        self.cmenu.append(item)
        self.sub_menu = Gtk.Menu()
        item.set_submenu(self.sub_menu)
        
        # Add item to submenu
        self.cm_item2 = Gtk.MenuItem.new_with_mnemonic('Submenu _Item')
        self.sub_menu.append(self.cm_item2)
        
        # Image Item - Build in icon-------------------------------
        img = Gtk.Image()
        # img.set_from_stock(Gtk.STOCK_NEW, 1)
        img.set_from_stock(Gtk.STOCK_DIRECTORY, 1)
        item = Gtk.ImageMenuItem('New')
        item.set_image(img)
        self.cmenu.append(item)
        
        # Image Item - Custom icon-------------------------------
        img = Gtk.Image()
        img.set_from_file('./image.png')
        imageItem = Gtk.ImageMenuItem(Gtk.STOCK_NEW, 'New')
        imageItem.set_image(img)
        self.cmenu.append(imageItem)
        
        # ------------------------------------
        
        self.cmenu.show_all()

    def on_menu_open():
        return True

    def _on_delete_event(self, a, b):
        Gtk.main_quit()

    def _on_button_press_event(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            self.cmenu.popup_at_pointer()

        return True # event was handled

if __name__ == '__main__':
    window = MyWindow()
    window.show_all()
    Gtk.main()