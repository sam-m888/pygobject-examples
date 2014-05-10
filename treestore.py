#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 250)
window.connect("destroy", lambda q: Gtk.main_quit())

treestore = Gtk.TreeStore(str)
dog = treestore.append(None, ["Dog"])
treestore.append(dog, ["Fido"])
treestore.append(dog, ["Spot"])
cat = treestore.append(None, ["Cat"])
treestore.append(cat, ["Ginger"])
rabbit = treestore.append(None, ["Rabbit"])
treestore.append(rabbit, ["Twitch"])
treestore.append(rabbit, ["Floppy"])

treeview = Gtk.TreeView(model=treestore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Pet Names")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

window.show_all()

Gtk.main()