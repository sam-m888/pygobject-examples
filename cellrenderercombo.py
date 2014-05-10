#!/usr/bin/env python

from gi.repository import Gtk

def combo_changed(cellrenderercombo, path, treeiter):    
    liststoreAppliance[path][1] = liststoreManufacturers[treeiter][0]
    
window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

liststoreAppliance = Gtk.ListStore(str, str)
liststoreAppliance.append(["Dishwasher", "Bosch"])
liststoreAppliance.append(["Refrigerator", "Samsung"])
liststoreAppliance.append(["Cooker", "Hotpoint"])

liststoreManufacturers = Gtk.ListStore(str)
liststoreManufacturers.append(["Bosch"])
liststoreManufacturers.append(["Whirlpool"])
liststoreManufacturers.append(["Hotpoint"])
liststoreManufacturers.append(["DeLonghi"])
liststoreManufacturers.append(["Samsung"])

treeview = Gtk.TreeView(model=liststoreAppliance)
treeviewcolumn = Gtk.TreeViewColumn("Appliance")
treeview.append_column(treeviewcolumn)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn.pack_start(cellrenderertext, False)
treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

treeviewcolumn = Gtk.TreeViewColumn("Manufacturer")
treeview.append_column(treeviewcolumn)
cellrenderercombo = Gtk.CellRendererCombo()
cellrenderercombo.set_property("editable", True)
cellrenderercombo.set_property("model", liststoreManufacturers)
cellrenderercombo.set_property("text-column", 0)
cellrenderercombo.connect("changed", combo_changed)
treeviewcolumn.pack_start(cellrenderercombo, False)
treeviewcolumn.add_attribute(cellrenderercombo, "text", 1)
window.add(treeview)

window.show_all()

Gtk.main()