#!/usr/bin/env python3

from gi.repository import Gtk

appchooserdialog = Gtk.AppChooserDialog(content_type="image/png")

response = appchooserdialog.run()

if response == Gtk.ResponseType.OK:
    app_info = appchooserdialog.get_app_info()
    display_name = app_info.get_display_name()
    description = app_info.get_description()
    
    print("Application selected")
    print("Name:\t\t%s" % display_name)
    print("Description:\t%s" % description)

appchooserdialog.destroy()