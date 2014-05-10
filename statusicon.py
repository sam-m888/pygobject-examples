#!/usr/bin/env python3

from gi.repository import Gtk

def popup_menu(icon, button, time):
    menu = Gtk.Menu()

    menuitemAbout = Gtk.MenuItem(label="About")
    menu.append(menuitemAbout)
    menuitemQuit = Gtk.MenuItem(label="Quit")
    menu.append(menuitemQuit)
    menu.show_all()

    menu.popup(None, None, None, None, button, time)

statusicon = Gtk.StatusIcon()
statusicon.set_from_stock(Gtk.STOCK_HOME)
statusicon.set_title("StatusIcon")
statusicon.connect("popup-menu", popup_menu)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())
window.show_all()

Gtk.main()