#!/usr/bin/env python3

from gi.repository import Gtk

def cell_edited(cellrendererspin, path, value):
    liststore[path][1] = int(value)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, int)
liststore.append(["Oranges", 5])
liststore.append(["Bananas", 2])
liststore.append(["Apples", 3])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Fruit")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, False)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

adjustment = Gtk.Adjustment(0, 0, 10, 1, 1, 0)
treeviewcolumn = Gtk.TreeViewColumn("Quantity")
treeview.append_column(treeviewcolumn)
cellrendererspin = Gtk.CellRendererSpin()
cellrendererspin.set_property("editable", True)
cellrendererspin.set_property("adjustment", adjustment)
cellrendererspin.connect("edited", cell_edited)
treeviewcolumn.pack_start(cellrendererspin, False)
treeviewcolumn.add_attribute(cellrendererspin, "text", 1)

window.show_all()

Gtk.main()