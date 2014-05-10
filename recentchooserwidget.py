#!/usr/bin/env python3

from gi.repository import Gtk

def item_activated(recentchoosermenu):
    item = recentchooserwidget.get_current_item()
    
    if item:
		name = item.get_display_name()
		uri = item.get_uri()
		
		print("Item selected:")
		print("Name:\t %s" % name)
		print("URI:\t %s" % uri)

window = Gtk.Window()
window.set_default_size(300, 250)
window.connect("destroy", lambda q: Gtk.main_quit())

recentchooserwidget = Gtk.RecentChooserWidget()
recentchooserwidget.connect("item-activated", item_activated)
window.add(recentchooserwidget)

window.show_all()

Gtk.main()