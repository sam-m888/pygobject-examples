#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

frame = Gtk.Frame(label="AspectFrame")
window.add(frame)

window.show_all()

Gtk.main()