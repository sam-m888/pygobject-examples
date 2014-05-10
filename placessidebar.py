#!/usr/bin/env python3

from gi.repository import Gtk, Gio

def open_link(placessiderbar, location, flags):
    location = placessidebar.get_location()

    print(GLocalFile.get_uri(location))

file = Gio.File.new_for_uri("/mnt/test")

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

placessidebar = Gtk.PlacesSidebar()
placessidebar.add_shortcut(file)
placessidebar.connect("open-location", open_link)
window.add(placessidebar)

window.show_all()

Gtk.main()