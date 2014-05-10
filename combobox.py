#!/usr/bin/env python3

from gi.repository import Gtk

def combobox_changed(combobox):
    treeiter = combobox.get_active_iter()
    print("ComboBox selected item: %s" % liststore[treeiter][0])

window = Gtk.Window()
window.set_default_size(150, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(str)
for item in ["Debian", "Sabayon", "Fedora", "Gentoo", "Tiny Core"]:
    liststore.append([item])

combobox = Gtk.ComboBox(model=liststore)
combobox.set_active(0)
combobox.connect("changed", combobox_changed)
window.add(combobox)

cellrenderertext = Gtk.CellRendererText()
combobox.pack_start(cellrenderertext, True)
combobox.add_attribute(cellrenderertext, "text", 0)

window.show_all()

Gtk.main()