#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
window.add(box)

sizegroup = Gtk.SizeGroup()
sizegroup.set_mode(Gtk.SizeGroupMode.HORIZONTAL)

button = Gtk.Button(label="Arch")
sizegroup.add_widget(button)
box.pack_start(button, True, True, 0)

button = Gtk.Button(label="Debian")
sizegroup.add_widget(button)
box.pack_start(button, True, True, 0)

button = Gtk.Button(label="OpenSuSE")
sizegroup.add_widget(button)
box.pack_start(button, True, True, 0)

window.show_all()

Gtk.main()