#!/usr/bin/env python3

from gi.repository import Gtk

fontchooserdialog = Gtk.FontChooserDialog(title="FontChooserDialog")

response = fontchooserdialog.run()

if response == Gtk.ResponseType.OK:
    print("Font selected: %s" % fontchooserdialog.get_font())

fontchooserdialog.destroy()