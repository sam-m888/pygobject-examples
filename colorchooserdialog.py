#!/usr/bin/env python3

from gi.repository import Gtk

def color_activated():
    color = colorchooserdialog.get_rgba()

    red = (color.red * 255)
    green = (color.green * 255)
    blue = (color.blue * 255)

    print("Hex: #%02x%02x%02x" % (red, green, blue))

colorchooserdialog = Gtk.ColorChooserDialog()

response = colorchooserdialog.run()
if response == Gtk.ResponseType.OK:
    color_activated()

colorchooserdialog.destroy()