#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(600, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

headerbar = Gtk.HeaderBar()
headerbar.set_title("Window Title")
headerbar.set_subtitle("Some subtitle text here")
headerbar.set_show_close_button(True)
window.add(headerbar)

label = Gtk.Label("Pack Start")
headerbar.pack_start(label)
label = Gtk.Label("Pack End")
headerbar.pack_end(label)

window.show_all()

Gtk.main()