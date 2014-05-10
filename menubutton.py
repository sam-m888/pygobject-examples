#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(50, 50)
window.connect("destroy", lambda q: Gtk.main_quit())

menubutton = Gtk.MenuButton()
window.add(menubutton)

menu = Gtk.Menu()
menubutton.set_popup(menu)

count = 1
while count < 6:
    menuitem = Gtk.MenuItem("Item %s" % count)
    menu.append(menuitem)
    menuitem.show()
    count += 1

window.show_all()

Gtk.main()