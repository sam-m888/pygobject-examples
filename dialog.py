#!/usr/bin/env python3

from gi.repository import Gtk

dialog = Gtk.Dialog(title="Dialog", buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
dialog.set_default_size(400, 300)

response = dialog.run()

if response == Gtk.ResponseType.OK:
    print("OK button clicked")
elif response == Gtk.ResponseType.CANCEL:
    print("Cancel button clicked")
else:
    print("Dialog closed")

dialog.destroy()