#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(250, 250)
window.connect("destroy", lambda q: Gtk.main_quit())

alignment = Gtk.Alignment()
alignment.set(0.50, 0.25, 0.0, 0.0)
window.add(alignment)

label = Gtk.Label(label="Aligment")
alignment.add(label)

window.show_all()

Gtk.main()