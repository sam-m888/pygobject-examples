#!/usr/bin/env python3

from gi.repository import Gtk, GdkPixbuf

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

liststore = Gtk.ListStore(GdkPixbuf.Pixbuf, str)

iconview = Gtk.IconView(model=liststore)
iconview.set_pixbuf_column(0)
iconview.set_text_column(1)
window.add(iconview)

image = Gtk.Image()

for item in ["fedora", "mandriva", "zenwalk", "knoppix", "debian"]:
    path = "../_resources/" + item + ".ico"
    image.set_from_file(path)
    pixbuf = image.get_pixbuf()
    liststore.append([pixbuf, item.capitalize()])

window.show_all()

Gtk.main()