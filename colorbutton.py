#!/usr/bin/env python3

from gi.repository import Gtk

def color_set(colorbutton):
    color = colorbutton.get_rgba()

    red = (color.red * 255)
    green = (color.green * 255)
    blue = (color.blue * 255)

    print("Hex: #%02x%02x%02x" % (red, green, blue))

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

colorbutton = Gtk.ColorButton()
colorbutton.connect("color-set", color_set)
window.add(colorbutton)

window.show_all()

Gtk.main()