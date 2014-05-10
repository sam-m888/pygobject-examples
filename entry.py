#!/usr/bin/env python3

from gi.repository import Gtk

def entry_activated(entry):
    print(entry.get_text())

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

entry = Gtk.Entry()
entry.connect("activate", entry_activated)
window.add(entry)

window.show_all()

Gtk.main()