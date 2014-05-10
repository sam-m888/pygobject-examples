#!/usr/bin/env python3

from gi.repository import Gtk

def font_changed(fontbutton):
    print("Font selected: %s" % fontbutton.get_font_name())

window = Gtk.Window()
window.set_default_size(150, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

fontbutton = Gtk.FontButton(title="FontButton")
fontbutton.connect("font-set", font_changed)
window.add(fontbutton)

window.show_all()

Gtk.main()