#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(400, 300)
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

stack = Gtk.Stack()
stack.set_hexpand(True)
stack.set_vexpand(True)
grid.attach(stack, 0, 1, 1, 1)

stackswitcher = Gtk.StackSwitcher()
stackswitcher.set_stack(stack)
grid.attach(stackswitcher, 0, 0, 1, 1)

for page in range(1, 4):
    label = Gtk.Label(label="Stack")
    stack.add_titled(label, "labelp1", "Page %s" % str(page))

window.show_all()

Gtk.main()