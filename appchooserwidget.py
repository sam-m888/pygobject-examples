#!/usr/bin/env python3

from gi.repository import Gtk

def application_activated(appchooserwidget, desktopappinfo):
    app_info = appchooserwidget.get_app_info()
    display_name = app_info.get_display_name()
    description = app_info.get_description()
    
    print("Application selected")
    print("Name:\t\t%s" % display_name)
    print("Description:\t%s" % description)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

appchooserwidget = Gtk.AppChooserWidget(content_type="video/webm")
appchooserwidget.connect("application-activated", application_activated)
window.add(appchooserwidget)

window.show_all()

Gtk.main()