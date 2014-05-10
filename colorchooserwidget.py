#!/usr/bin/env python3

from gi.repository import Gtk

def color_activated(colorchooserwidget, color):
    red = (color.red * 255)
    green = (color.green * 255)
    blue = (color.blue * 255)

    print("Hex: #%02x%02x%02x" % (red, green, blue))

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

colorchooserwidget = Gtk.ColorChooserWidget()
colorchooserwidget.connect("color-activated", color_activated)
window.add(colorchooserwidget)

window.show_all()

Gtk.main()