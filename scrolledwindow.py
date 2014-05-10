#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

scrolledwindow = Gtk.ScrolledWindow()
window.add(scrolledwindow)

layout = Gtk.Layout()
layout.set_size(800, 600)
layout.set_vexpand(True)
layout.set_hexpand(True)
scrolledwindow.add(layout)

hadjustment = layout.get_hadjustment()
scrolledwindow.set_hadjustment(hadjustment)
vadjustment = layout.get_vadjustment()
scrolledwindow.set_vadjustment(vadjustment)

button = Gtk.Button(label="Button 1")
layout.put(button, 645, 140)
button = Gtk.Button(label="Button 2")
layout.put(button, 130, 225)
button = Gtk.Button(label="Button 3")
layout.put(button, 680, 350)

window.show_all()

Gtk.main()