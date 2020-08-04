#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        self.cmenu = Gtk.Menu.new()
        self.cm_item = Gtk.MenuItem.new_with_label('label')
        self.cmenu.append(self.cm_item)
        self.cmenu.show_all()

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