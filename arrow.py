#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 50)
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=True)
window.add(box)

arrow = Gtk.Arrow(arrow_type=Gtk.ArrowType.UP, shadow_type=Gtk.ShadowType.NONE)
box.pack_start(arrow, True, True, 0)
arrow = Gtk.Arrow(arrow_type=Gtk.ArrowType.DOWN, shadow_type=Gtk.ShadowType.NONE)
box.pack_start(arrow, True, True, 0)
arrow = Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
box.pack_start(arrow, True, True, 0)
arrow = Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
box.pack_start(arrow, True, True, 0)

window.show_all()

Gtk.main()