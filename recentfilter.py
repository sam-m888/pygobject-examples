#!/usr/bin/env python3

from gi.repository import Gtk

recentchooserdialog = Gtk.RecentChooserDialog()
recentchooserdialog.set_default_size(300, 200)

recentfilter = Gtk.RecentFilter()
recentfilter.set_name("All Items")
recentfilter.add_pattern("*")
recentchooserdialog.add_filter(recentfilter)

recentfilter = Gtk.RecentFilter()
recentfilter.set_name("Within last 3 days")
recentfilter.add_age(3)
recentchooserdialog.add_filter(recentfilter)

recentfilter = Gtk.RecentFilter()
recentfilter.set_name("Image Files")
recentfilter.add_pattern("*.png")
recentfilter.add_pattern("*.jpg")
recentfilter.add_pattern("*.svg")
recentchooserdialog.add_filter(recentfilter)

recentchooserdialog.run()
recentchooserdialog.destroy()