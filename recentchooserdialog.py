#!/usr/bin/env python3

from gi.repository import Gtk

recentchooserdialog = Gtk.RecentChooserDialog()
recentchooserdialog.set_title("RecentChooserDialog")
recentchooserdialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
recentchooserdialog.add_button("OK", Gtk.ResponseType.OK)
recentchooserdialog.set_default_size(400, -1)

response = recentchooserdialog.run()

if response == Gtk.ResponseType.OK:
    item = recentchooserdialog.get_current_item()
    
    if item:
		name = item.get_display_name()
		uri = item.get_uri()
		
		print("Item selected:")
		print("Name:\t %s" % name)
		print("URI:\t %s" % uri)
		

recentchooserdialog.destroy()