#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

toolpalette = Gtk.ToolPalette()
window.add(toolpalette)

toolitemgroup = Gtk.ToolItemGroup(label="Group 1")
toolpalette.add(toolitemgroup)

toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_NEW)
toolitemgroup.insert(toolbutton, 0)
toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_OPEN)
toolitemgroup.insert(toolbutton, 1)
toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_SAVE)
toolitemgroup.insert(toolbutton, 2)

toolitemgroup = Gtk.ToolItemGroup(label="Group 2")
toolpalette.add(toolitemgroup)

toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_ABOUT)
toolitemgroup.insert(toolbutton, 0)
toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_PREFERENCES)
toolitemgroup.insert(toolbutton, 1)

window.show_all()

Gtk.main()