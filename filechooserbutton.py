#!/usr/bin/env python3

from gi.repository import Gtk

def file_changed(filechooserbutton):
    print("File selected: %s" % filechooserbutton.get_filename())

window = Gtk.Window()
window.set_default_size(150, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

filechooserbutton = Gtk.FileChooserButton(title="FileChooserButton")
filechooserbutton.connect("file-set", file_changed)
window.add(filechooserbutton)

window.show_all()

Gtk.main()