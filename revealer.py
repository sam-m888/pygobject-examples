#!/usr/bin/env python3

from gi.repository import Gtk

def reveal_child(button):
    if revealer.get_reveal_child():
        revealer.set_reveal_child(False)
    else:
        revealer.set_reveal_child(True)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

revealer = Gtk.Revealer()
revealer.set_reveal_child(True)
grid.attach(revealer, 0, 0, 1, 1)

label = Gtk.Label("Label contained in a Revealer widget")
revealer.add(label)

button = Gtk.Button("Reveal")
button.connect("clicked", reveal_child)
grid.attach(button, 0, 1, 1, 1)

window.show_all()

Gtk.main()