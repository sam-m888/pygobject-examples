#!/usr/bin/env python3

from gi.repository import Gtk

def display_value(scalebutton, value):
    print("ScaleButton value: %0.2f" % value)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

scalebutton = Gtk.ScaleButton()
scalebutton.connect("value-changed", display_value)
window.add(scalebutton)

window.show_all()

Gtk.main()