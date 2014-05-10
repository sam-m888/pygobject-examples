#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
grid.set_row_spacing(5)
grid.set_column_spacing(5)
window.add(grid)

button = Gtk.Button(label="Button 1")
grid.attach(button, 0, 0, 1, 2)
button = Gtk.Button(label="Button 2")
grid.attach(button, 1, 0, 1, 1)
button = Gtk.Button(label="Button 3")
grid.attach(button, 2, 0, 1, 1)
button = Gtk.Button(label="Button 4")
grid.attach(button, 1, 1, 2, 1)

window.show_all()

Gtk.main()