#!/usr/bin/env python3

from gi.repository import Gtk

def close_hello_world(widget):
    Gtk.main_quit()
    
def print_hello_world(widget):
    print("Hello World")

window = Gtk.Window()
window.connect("destroy", close_hello_world)
        
button = Gtk.Button("Click here")
button.connect("clicked", print_hello_world)
window.add(button)
        
window.show_all()

Gtk.main()