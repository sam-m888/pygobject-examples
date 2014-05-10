#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(400, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
box.set_homogeneous(True)
window.add(box)

separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
box.pack_start(separator, True, True, 0)

separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
box.pack_start(separator, True, True, 0)

window.show_all()

Gtk.main()