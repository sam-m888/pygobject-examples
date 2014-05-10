#!/usr/bin/env python3

from gi.repository import Gtk
import sys

def embed_event(widget):
    print("A plug has been embedded")

if len(sys.argv) == 2:
	socket_id = sys.argv[1]
	socket_id = int(socket_id)

plug = Gtk.Plug.new(socket_id)
plug.connect("embedded", embed_event)
plug.connect("destroy", lambda q: Gtk.main_quit())

print("Plug ID:", plug.get_id())

entry = Gtk.Entry()
plug.add(entry)

plug.show_all()

Gtk.main()