#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

toolbar = Gtk.Toolbar()
window.add(toolbar)

toolbutton1 = Gtk.RadioToolButton(stock_id=Gtk.STOCK_PREFERENCES, group=None)
toolbutton1.set_is_important(True)
toolbar.insert(toolbutton1, 0)
toolbutton2 = Gtk.RadioToolButton(stock_id=Gtk.STOCK_ABOUT, group=toolbutton1)
toolbar.insert(toolbutton2, 1)
toolbutton3 = Gtk.RadioToolButton(stock_id=Gtk.STOCK_HELP, group=toolbutton1)
toolbar.insert(toolbutton3, 2)

window.show_all()

Gtk.main()