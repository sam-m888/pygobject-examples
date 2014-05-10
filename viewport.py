#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

viewport = Gtk.Viewport()
viewport.set_size_request(200, 200)
grid.attach(viewport, 0, 0, 1, 1)

vadjustment = viewport.get_vadjustment()
hadjustment = viewport.get_hadjustment()

vscrollbar = Gtk.VScrollbar()
grid.attach(vscrollbar, 1, 0, 1, 1)
hscrollbar = Gtk.HScrollbar()
grid.attach(hscrollbar, 0, 1, 1, 1)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
viewport.add(box)

for i in range(0, 15):
    button = Gtk.Button(label="Button %s" % i)
    box.pack_start(button, True, True, 0)

window.show_all()

Gtk.main()