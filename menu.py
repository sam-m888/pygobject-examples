#!/usr/bin/env python3

from gi.repository import Gtk

def event(widget, event):
    if event.button == 3:
        menu.popup(None, None, None, None, event.button, event.time)
        menu.show_all()
    
    return True
    
window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

menubar = Gtk.MenuBar()
menubar.set_hexpand(True)
grid.attach(menubar, 0, 0, 1, 1)

menuitem = Gtk.MenuItem(label="MenuItem")
menubar.append(menuitem)
menu = Gtk.Menu()
menuitem.set_submenu(menu)
menuitem = Gtk.MenuItem(label="MenuItem")
menu.append(menuitem)

menuitem = Gtk.MenuItem(label="CheckMenuItem")
menubar.append(menuitem)
menu = Gtk.Menu()
menuitem.set_submenu(menu)
checkmenuitem = Gtk.CheckMenuItem(label="CheckMenuItem")
menu.append(checkmenuitem)

menuitem = Gtk.MenuItem(label="RadioMenuItem")
menubar.append(menuitem)
menu = Gtk.Menu()
menuitem.set_submenu(menu)
radiomenuitem1 = Gtk.RadioMenuItem(label="RadioMenuItem 1")
radiomenuitem1.set_active(True)
menu.append(radiomenuitem1)
radiomenuitem2 = Gtk.RadioMenuItem(label="RadioMenuItem 2", group=radiomenuitem1)
menu.append(radiomenuitem2)

eventbox = Gtk.EventBox()
eventbox.set_size_request(-1, 200)
eventbox.connect("button-release-event", event)
grid.attach(eventbox, 0, 1, 1, 1)

window.show_all()

Gtk.main()