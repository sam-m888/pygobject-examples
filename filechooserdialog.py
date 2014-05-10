#!/usr/bin/env python3

from gi.repository import Gtk

filechooserdialog = Gtk.FileChooserDialog(title="FileChooserDialog", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

response = filechooserdialog.run()

if response == Gtk.ResponseType.OK:
    print("File selected: %s" % filechooserdialog.get_filename())

filechooserdialog.destroy()