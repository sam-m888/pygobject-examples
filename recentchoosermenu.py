#!/usr/bin/env python3

from gi.repository import Gtk

def item_activated(recentchoosermenu):
    item = recentchoosermenu.get_current_item()
    
    if item:
		name = item.get_display_name()
		uri = item.get_uri()
		
		print("Item selected:")
		print("Name:\t %s" % name)
		print("URI:\t %s" % uri)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

menubar = Gtk.MenuBar()
window.add(menubar)

menuitem = Gtk.MenuItem(label="Recent Items")
menubar.append(menuitem)

recentchoosermenu = Gtk.RecentChooserMenu()
recentchoosermenu.connect("item-activated", item_activated)
menuitem.set_submenu(recentchoosermenu)

window.show_all()

Gtk.main()