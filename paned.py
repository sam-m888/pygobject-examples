#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(400, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

hpaned = Gtk.Paned()
hpaned.set_position(150)
window.add(hpaned)

label = Gtk.Label(label="Left Pane")
hpaned.add1(label)

vpaned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
vpaned.set_position(75)
hpaned.add2(vpaned)

label = Gtk.Label(label="Top Right Pane")
vpaned.add1(label)

label = Gtk.Label(label="Bottom Right Pane")
vpaned.add2(label)

window.show_all()

Gtk.main()