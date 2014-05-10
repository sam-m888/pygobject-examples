#!/usr/bin/env python3

from gi.repository import Gtk, GdkPixbuf

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, GdkPixbuf.Pixbuf)

icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/fedora.ico", 16, 16)
liststore.append(["Fedora", icon])
icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/opensuse.ico", 16, 16)
liststore.append(["OpenSuSE", icon])
icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/gentoo.ico", 16, 16)
liststore.append(["Gentoo", icon])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Distribution")
treeview.append_column(treeviewcolumn)

cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, True)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Logo")
treeview.append_column(treeviewcolumn)

cellrendererpixbuf = Gtk.CellRendererPixbuf()
treeviewcolumn.pack_start(cellrendererpixbuf, False)
treeviewcolumn.add_attribute(cellrendererpixbuf, "pixbuf", 1)

window.show_all()

Gtk.main()