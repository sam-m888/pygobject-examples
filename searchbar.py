#!/usr/bin/env python3

from gi.repository import Gtk, Gdk

def find_event(widget, event=None):
    keyval = event.keyval
    name = Gdk.keyval_name(keyval)
    mod = Gtk.accelerator_get_label(keyval, event.state)

    if mod == "Ctrl+F" or mod == "Ctrl+Mod2+F":
        if searchbar.get_search_mode():
            searchbar.set_search_mode(False)
        else:
            searchbar.set_search_mode(True)

window = Gtk.Window()
window.set_default_size(250, -1)
window.connect("key-press-event", find_event)
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

label = Gtk.Label("Press Control+F to initiate find")
label.set_size_request(100, 100)
grid.attach(label, 0, 0, 1, 1)

searchbar = Gtk.SearchBar()
grid.attach(searchbar, 0, 1, 1, 1)

searchentry = Gtk.SearchEntry()
searchbar.connect_entry(searchentry)
searchbar.add(searchentry)

window.show_all()

Gtk.main()