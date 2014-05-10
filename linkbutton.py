#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

linkbutton = Gtk.LinkButton(uri="http://example.com", label="Example")
window.add(linkbutton)

window.show_all()

Gtk.main()