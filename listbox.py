#!/usr/bin/env python3

from gi.repository import Gtk

def row_activated(listbox, listboxrow):
    print("Row %i activated" % listboxrow.get_index())

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

listbox = Gtk.ListBox()
listbox.connect("row-activated", row_activated)
window.add(listbox)

label = Gtk.Label("Row 1")
listbox.insert(label, 0)

button = Gtk.Button(label="Row 2")
listbox.insert(button, 1)

grid = Gtk.Grid()
listbox.insert(grid, 2)
label = Gtk.Label("Row 3")
grid.attach(label, 0, 0, 1, 1)
checkbutton = Gtk.CheckButton()
grid.attach(checkbutton, 1, 0, 1, 1)

window.show_all()

Gtk.main()