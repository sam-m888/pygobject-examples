#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_border_width(5)
window.connect("destroy", lambda q: Gtk.main_quit())

label = Gtk.Label(label="Hover over this Label")
label.set_tooltip_text("This is an example of the basic Tooltip")
window.add(label)

window.show_all()

Gtk.main()