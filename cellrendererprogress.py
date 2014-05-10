#!/usr/bin/env python3

from gi.repository import Gtk, GObject
import random

def pulse_progressbar():
    for item in liststore:
        if item[1] < 100:
            value = random.randint(0, 5)
            
            if value + item[1] > 100:
                item[1] = 100
            else:
                item[1] += value
        else:
            item[1] = 0
    
    return True

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str, int)
liststore.append(["Downloading files", 0])
liststore.append(["Parsing access logs", 0])
liststore.append(["Compiling modules", 0])

treeview = Gtk.TreeView(model=liststore)
window.add(treeview)

treeviewcolumn = Gtk.TreeViewColumn("Action")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, False)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Status")
treeview.append_column(treeviewcolumn)
cellrendererprogress = Gtk.CellRendererProgress()
treeviewcolumn.pack_start(cellrendererprogress, True)
treeviewcolumn.add_attribute(cellrendererprogress, "value", 1)

window.show_all()

GObject.timeout_add(250, pulse_progressbar)

Gtk.main()