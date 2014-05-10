#!/usr/bin/env python3

from gi.repository import Gtk

def radiobutton_toggled(radiobutton):
    if radiobutton.get_active():
        print("%s is active" % radiobutton.get_label())

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(box)

radiobutton1 = Gtk.RadioButton(label="RadioButton 1")
radiobutton1.connect("toggled", radiobutton_toggled)
box.pack_start(radiobutton1, True, True, 0)
radiobutton2 = Gtk.RadioButton(label="RadioButton 2", group=radiobutton1)
radiobutton2.connect("toggled", radiobutton_toggled)
box.pack_start(radiobutton2, True, True, 0)
radiobutton3 = Gtk.RadioButton(label="RadioButton 3", group=radiobutton1)
radiobutton3.connect("toggled", radiobutton_toggled)
box.pack_start(radiobutton3, True, True, 0)

window.show_all()

Gtk.main()