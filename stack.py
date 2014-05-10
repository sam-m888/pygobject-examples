#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(400, 300)
window.connect("destroy", lambda q: Gtk.main_quit())

stack = Gtk.Stack()
window.add(stack)

label = Gtk.Label("Stack Widget")
stack.add_named(label, "label")

window.show_all()

Gtk.main()