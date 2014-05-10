#!/usr/bin/env python3

from gi.repository import Gtk, GObject

def pulse_spinner():    
    for item in liststore:
        if item[1] == True:
            if item[2] == 12:
                item[2] = 0
            else:
                item[2] += 1
    
    cellrendererspinner.set_property("pulse", item[2])
    
    return True

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, bool, int)
liststore.append(["Copying files", True,  0])
liststore.append(["Downloading access logs", False, 0])
liststore.append(["Connecting to server", True, 0])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Activity")
treeview.append_column(treeviewcolumn)

cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, False)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Status")
treeview.append_column(treeviewcolumn)

cellrendererspinner = Gtk.CellRendererSpinner()
treeviewcolumn.pack_start(cellrendererspinner, False)
treeviewcolumn.add_attribute(cellrendererspinner, "active", 1)

window.show_all()

GObject.timeout_add(100, pulse_spinner)

Gtk.main()