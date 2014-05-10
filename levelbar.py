#!/usr/bin/env python3

from gi.repository import Gtk
import random

window = Gtk.Window()
window.set_default_size(150, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

levelbar = Gtk.LevelBar()
levelbar.set_min_value(0)
levelbar.set_max_value(10)
levelbar.set_value(random.randint(0, 10))
window.add(levelbar)

window.show_all()

Gtk.main()