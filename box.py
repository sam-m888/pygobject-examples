#/usr/bin/env python3
  
from gi.repository import Gtk

window = Gtk.Window()

box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
window.add(box)

label = Gtk.Label("Label 1")
box.pack_start(label, True, True, 0)
label = Gtk.Label("Label 2")
box.pack_start(label, True, True, 0)

window.show_all()

Gtk.main()