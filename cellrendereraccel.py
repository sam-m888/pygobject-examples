#!/usr/bin/env python3

from gi.repository import Gtk

def accel_edited(cellrendereraccel, path, key, mods, hwcode):
    accelerator = Gtk.accelerator_name(key, mods)
    liststore[path][1] = accelerator

def accel_cleared(cellrendereraccel, path):
    liststore[path][1] = "None"

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, str)
liststore.append(["New", "<Primary>n"])
liststore.append(["Open", "<Primary>o"])
liststore.append(["Save", "<Primary>s"])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Action")
treeview.append_column(treeviewcolumn)

cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Accelerator")
treeview.append_column(treeviewcolumn)

cellrendereraccel = Gtk.CellRendererAccel()
cellrendereraccel.set_property("editable", True)
cellrendereraccel.connect("accel-edited", accel_edited)
cellrendereraccel.connect("accel-cleared", accel_cleared)
treeviewcolumn.pack_start(cellrendereraccel, True)
treeviewcolumn.add_attribute(cellrendereraccel, "text", 1)

window.show_all()

Gtk.main()