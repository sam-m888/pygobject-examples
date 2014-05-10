#!/usr/bin/env python3

from gi.repository import Gtk

def cell_edited(cellrenderertext, path, text):
    liststore[path][1] = text

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, str)
liststore.append(["Fedora", "http://fedoraproject.org/"])
liststore.append(["Ubuntu", "http://www.ubuntu.com/"])
liststore.append(["Slackware", "http://www.slackware.com/"])

treeview = Gtk.TreeView(model=liststore)
treeviewcolumn = Gtk.TreeViewColumn("Distribution")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)
treeviewcolumn = Gtk.TreeViewColumn("Website")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
cellrenderertext.set_property("editable", True)
cellrenderertext.connect("edited", cell_edited)
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 1)
window.add(treeview)

window.show_all()

Gtk.main()