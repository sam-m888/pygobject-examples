#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

adjustment = Gtk.Adjustment(value=0, lower=-10, upper=25, step_increment=1, page_increment=5, page_size=0)
spinbutton = Gtk.SpinButton(adjustment=adjustment)
window.add(spinbutton)

window.show_all()

Gtk.main()