#!/usr/bin/env python3

from gi.repository import Gtk

def switch_toggled(switch, state):
    if switch.get_active():
        print("Switch toggled to on")
    else:
        print("Switch toggled to off")

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

switch = Gtk.Switch()
switch.connect("notify::active", switch_toggled)
window.add(switch)

window.show_all()

Gtk.main()