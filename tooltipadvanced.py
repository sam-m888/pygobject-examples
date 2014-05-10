#!/usr/bin/env python3

from gi.repository import Gtk

def tooltip_query(widget, x, y, keyboard_mode, tooltip):
    tooltip.set_text("This is an example of the advanced Tooltip")
    
    return True

window = Gtk.Window()
window.set_border_width(5)
window.connect("destroy", lambda q: Gtk.main_quit())

tooltip = Gtk.Tooltip()

label = Gtk.Label(label="Hover over this Label")
label.set_has_tooltip(True)
label.connect("query-tooltip", tooltip_query)
window.add(label)

window.show_all()

Gtk.main()