#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

layout = Gtk.Layout()
window.add(layout)

button = Gtk.Button(label="Button 1")
layout.put(button, 40, 60)
button = Gtk.Button(label="Button 2")
layout.put(button, 155, 80)

window.show_all()

Gtk.main()