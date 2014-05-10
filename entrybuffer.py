#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
window.add(box)

entrybuffer = Gtk.EntryBuffer(text="Text in EntryBuffer")

entry = Gtk.Entry(buffer=entrybuffer)
box.pack_start(entry, True, True, 0)
entry = Gtk.Entry(buffer=entrybuffer)
box.pack_start(entry, True, True, 0)
entry = Gtk.Entry(buffer=entrybuffer)
box.pack_start(entry, True, True, 0)

window.show_all()

Gtk.main()