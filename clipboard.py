#!/usr/bin/env python3

from gi.repository import Gtk, Gdk

def copy_text(button, action):
    content = entry.get_text()
    
    if action == "cut":
        entry.set_text("")
    
    clipboard.set_text(content, -1)

def paste_text(button):
    content = clipboard.wait_for_text()
    entry.set_text(content)

clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

entry = Gtk.Entry()
grid.attach(entry, 0, 0, 1, 1)

buttonCutText = Gtk.Button(label="Cut Text")
buttonCutText.connect("clicked", copy_text, "cut")
grid.attach(buttonCutText, 1, 0, 1, 1)

buttonCopyText = Gtk.Button(label="Copy Text")
buttonCopyText.connect("clicked", copy_text, "copy")
grid.attach(buttonCopyText, 2, 0, 1, 1)

buttonPasteText = Gtk.Button(label="Paste Text")
buttonPasteText.connect("clicked", paste_text)
grid.attach(buttonPasteText, 3, 0, 1, 1)

window.show_all()

Gtk.main()