#!/usr/bin/env python3

from gi.repository import Gtk

def checkbutton_toggled(checkbutton):
    if checkbutton.get_active():
        print("CheckButton has been toggled on!")
    else:
        print("CheckButton has been toggled off!")

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

checkbutton = Gtk.CheckButton(label="CheckButton")
checkbutton.connect("toggled", checkbutton_toggled)
window.add(checkbutton)

window.show_all()

Gtk.main()