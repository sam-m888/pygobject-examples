#!/usr/bin/env python3

from gi.repository import Gtk

def togglebutton_toggled(togglebutton):
    if togglebutton.get_active():
        spinner.start()
    else:
        spinner.stop()

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

spinner = Gtk.Spinner()
spinner.set_vexpand(True)
spinner.set_hexpand(True)
grid.attach(spinner, 0, 0, 1, 1)

togglebutton = Gtk.ToggleButton(label="Start / Stop")
togglebutton.connect("toggled", togglebutton_toggled)
grid.attach(togglebutton, 0, 1, 1, 1)

window.show_all()

Gtk.main()