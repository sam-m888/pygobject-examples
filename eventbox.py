#!/usr/bin/env python3

from gi.repository import Gtk

def event(eventbox, event):
    print("Event: %s" % event)

def event_press(eventbox, event):
    print("Button Press Event: %s" % event)

def event_release(eventbox, event):
    print("Button Release Event: %s" % event)

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

eventbox = Gtk.EventBox()
eventbox.connect("event", event)
eventbox.connect("button-press-event", event_press)
eventbox.connect("button-release-event", event_release)
window.add(eventbox)

label = Gtk.Label("EventBox containing Label")
eventbox.add(label)

window.show_all()

Gtk.main()