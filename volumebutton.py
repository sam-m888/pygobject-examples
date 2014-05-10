#!/usr/bin/env python3

from gi.repository import Gtk

def display_value(volumebutton, value):
    print("VolumeButton value: %0.2f" % value)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

volumebutton = Gtk.VolumeButton()
volumebutton.connect("value-changed", display_value)
window.add(volumebutton)

window.show_all()

Gtk.main()