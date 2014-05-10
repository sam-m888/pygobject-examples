#!/usr/bin/env python3

from gi.repository import Gtk, GObject

def update_progressbar():
    fraction = progressbar.get_fraction()
    
    if fraction < 1.0:    
        progressbar.set_fraction(fraction + 0.1)
    else:
        progressbar.set_fraction(0.0)
    
    return True

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

progressbar = Gtk.ProgressBar()
progressbar.set_show_text(True)
window.add(progressbar)

window.show_all()

GObject.timeout_add(1000, update_progressbar)

Gtk.main()