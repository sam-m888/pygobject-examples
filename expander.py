#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

expander = Gtk.Expander(label="Expander")
expander.set_resize_toplevel(True)
window.add(expander)

button = Gtk.Button(label="Button")
button.set_size_request(100, 100)
expander.add(button)

window.show_all()

Gtk.main()