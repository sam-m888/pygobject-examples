#!/usr/bin/env python3

from gi.repository import Gtk, Gdk

def button_clicked(widget):
    print("Save button clicked")

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

accelgroup = Gtk.AccelGroup()
window.add_accel_group(accelgroup)

accellabel = Gtk.AccelLabel("Button accelerator:")
accellabel.set_hexpand(True)
grid.attach(accellabel, 0, 0, 2, 1)

button = Gtk.Button("Save")
button.add_accelerator("clicked", accelgroup, Gdk.keyval_from_name("s"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
button.connect("clicked", button_clicked)
accellabel.set_accel_widget(button)
grid.attach(button, 0, 1, 2, 1)

window.show_all()

Gtk.main()