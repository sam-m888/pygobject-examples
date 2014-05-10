#!/usr/bin/env python3

from gi.repository import Gtk

def item_changed(appchooserbutton):
    app_info = appchooserbutton.get_app_info()
    display_name = app_info.get_display_name()
    description = app_info.get_description()
    
    print("Application selected")
    print("Name:\t\t%s" % display_name)
    print("Description:\t%s" % description)

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

appchooserbutton = Gtk.AppChooserButton(content_type="audio/flac")
appchooserbutton.set_show_dialog_item(True)
appchooserbutton.connect("changed", item_changed)
window.add(appchooserbutton)

window.show_all()

Gtk.main()