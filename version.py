#!/usr/bin/env python3

from gi.repository import Gtk

major = Gtk.get_major_version()
minor = Gtk.get_minor_version()
micro = Gtk.get_micro_version()

print("GTK version number is %i.%i.%i" % (major, minor, micro))