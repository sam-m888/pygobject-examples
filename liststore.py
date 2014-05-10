#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, int)
liststore.append(["Oranges", 5])
liststore.append(["Apples", 3])
liststore.append(["Bananas", 1])
liststore.append(["Tomatoes", 4])
liststore.append(["Cucumber", 1])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Item")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Quantity")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 1)

window.show_all()

Gtk.main()