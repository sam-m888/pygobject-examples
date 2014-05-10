#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

image = Gtk.Image()
image.set_from_file("gtk.png")
window.add(image)

window.show_all()

Gtk.main()