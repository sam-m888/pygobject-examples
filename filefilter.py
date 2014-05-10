#!/usr/bin/env python3

from gi.repository import Gtk

filechooserdialog = Gtk.FileChooserDialog()

filefilter = Gtk.FileFilter()
filefilter.set_name("All Items")
filefilter.add_pattern("*")
filechooserdialog.add_filter(filefilter)
filefilter = Gtk.FileFilter()
filefilter.set_name("Audio")
filefilter.add_mime_type("audio/flac")
filefilter.add_mime_type("audio/ogg")
filechooserdialog.add_filter(filefilter)
filefilter = Gtk.FileFilter()
filefilter.set_name("Images")
filefilter.add_pattern("*.png")
filefilter.add_pattern("*.jpg")
filefilter.add_pattern("*.bmp")
filechooserdialog.add_filter(filefilter)

filechooserdialog.run()
filechooserdialog.destroy()