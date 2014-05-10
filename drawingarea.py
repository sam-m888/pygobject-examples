#!/usr/bin/env python3

from gi.repository import Gtk, GdkX11
import cairo

def expose(drawingarea, context):
    

window = Gtk.Window()
window.set_default_size(600, 400)
window.connect("destroy", lambda q: Gtk.main_quit())

drawingarea = Gtk.DrawingArea()

drawingarea.connect("draw", expose)
window.add(drawingarea)
window.show_all()

Gtk.main()