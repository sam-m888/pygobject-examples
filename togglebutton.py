#!/usr/bin/env python3

from gi.repository import Gtk

def togglebutton_toggled(togglebutton):
    print("ToggleButton has been toggled!")

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

togglebutton = Gtk.ToggleButton(label="ToggleButton")
togglebutton.connect("toggled", togglebutton_toggled)
window.add(togglebutton)

window.show_all()

Gtk.main()