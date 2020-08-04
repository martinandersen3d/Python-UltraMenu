import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win  = Gtk.Window ()
box  = Gtk.EventBox ()
area = Gtk.DrawingArea ()

def onclick (box, event):
    return True
    print(event.x, event.y)

box.connect ('button-press-event', onclick)

box.add (area)
win.add (box)
win.show_all ()
win.connect ('destroy', lambda *x: Gtk.main_quit ())
