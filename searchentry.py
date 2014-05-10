#!/usr/bin/env python3

from gi.repository import Gtk

def search_changed(searchentry):
    print(searchentry.get_text())

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

searchentry = Gtk.SearchEntry()
searchentry.connect("search-changed", search_changed)
window.add(searchentry)

window.show_all()

Gtk.main()