#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

label = Gtk.Label(label="GTK+, or the GIMP Toolkit, is a multi-platform\ntoolkit for creating graphical user interfaces.\nOffering a complete set of widgets, GTK+ is\nsuitablefor projects ranging from small one-off\ntools to complete application suites.")
window.add(label)

window.show_all()

Gtk.main()