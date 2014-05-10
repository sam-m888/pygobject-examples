#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

buttonbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)
buttonbox.set_spacing(2)
window.add(buttonbox)

button = Gtk.Button(stock=Gtk.STOCK_OK)
buttonbox.add(button)
button = Gtk.Button(stock=Gtk.STOCK_CANCEL)
buttonbox.add(button)
button = Gtk.Button(stock=Gtk.STOCK_APPLY)
buttonbox.add(button)

window.show_all()

Gtk.main()