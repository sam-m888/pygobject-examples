#!/usr/bin/env python3

from gi.repository import Gtk

aboutdialog = Gtk.AboutDialog()
aboutdialog.set_name("Test")
aboutdialog.set_version("1.0")
aboutdialog.set_comments("Some random comment")
aboutdialog.set_website("http://example.com/")
aboutdialog.set_website_label("Random Label")
aboutdialog.set_authors(["Unknown author"])

aboutdialog.run()
aboutdialog.destroy()