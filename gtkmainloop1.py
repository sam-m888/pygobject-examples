#!/usr/bin/env python3

from gi.repository import Gtk

class HelloWorld:
    def close_hello_world(self, widget):
        Gtk.main_quit()

    def print_hello_world(self, widget):
        print("Hello World")

    def __init__(self):
        window = Gtk.Window()
        window.connect("destroy", self.close_hello_world)

        button = Gtk.Button("Click here")
        button.connect("clicked", self.print_hello_world)
        window.add(button)

        window.show_all()

HelloWorld()
Gtk.main()