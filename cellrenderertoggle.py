#!/usr/bin/env python3

from gi.repository import Gtk

def cell_toggled(cellrenderertoggle, path):
    liststore[path][1] = not liststore[path][1]

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, bool)
liststore.append(["Ethernet", True])
liststore.append(["Wireless", True])
liststore.append(["Bluetooth", False])
liststore.append(["3g Mobile", True])

treeview = Gtk.TreeView(model=liststore)
treeviewcolumn = Gtk.TreeViewColumn("Connection Type")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, False)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)
treeviewcolumn = Gtk.TreeViewColumn("Status")
treeview.append_column(treeviewcolumn)
cellrenderertoggle = Gtk.CellRendererToggle()
cellrenderertoggle.connect("toggled", cell_toggled)
treeviewcolumn.pack_start(cellrenderertoggle, False)
treeviewcolumn.add_attribute(cellrenderertoggle, "active", 1)
window.add(treeview)

window.show_all()

Gtk.main()