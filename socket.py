#!/usr/bin/env python3

from gi.repository import Gtk
import sys

def plug_event(widget):
    print("A plug has been inserted")

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

socket = Gtk.Socket()
socket.connect("plug-added", plug_event)
window.add(socket)

print("Socket ID:", socket.get_id())

if len(sys.argv) == 2:
    pid = int(sys.argv[1])
    socket.add_id(pid)

window.show_all()

Gtk.main()