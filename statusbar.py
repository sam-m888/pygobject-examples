#!/usr/bin/env python3

from gi.repository import Gtk

count = 0

def push_message(widget):
    global count
    count += 1
    
    message = "Message number %i" % count
    statusbar.push(context, message)

def pop_message(widget):
    statusbar.pop(context)

def remove_messages(widget):
    statusbar.remove_all(context)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
grid.set_column_spacing(5)
window.add(grid)

buttonPush = Gtk.Button("Push message")
buttonPush.connect("clicked", push_message)
grid.attach(buttonPush, 0, 0, 1, 1)

buttonPop = Gtk.Button("Pop message")
buttonPop.connect("clicked", pop_message)
grid.attach(buttonPop, 1, 0, 1, 1)

buttonRemove = Gtk.Button("Remove all")
buttonRemove.connect("clicked", remove_messages)
grid.attach(buttonRemove, 2, 0, 1, 1)

statusbar = Gtk.Statusbar()
context = statusbar.get_context_id("example")
grid.attach(statusbar, 0, 1, 3, 1)

window.show_all()

Gtk.main()