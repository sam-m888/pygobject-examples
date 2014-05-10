#!/usr/bin/env python3

from gi.repository import Gtk

def file_selected(button):
    print("Selected file: %s" % filechooserwidget.get_filename())
    Gtk.main_quit()

window = Gtk.Window()
window.set_default_size(600, 400)
window.set_border_width(2)
window.connect("destroy", lambda q: Gtk.main_quit())

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
window.add(box)

filechooserwidget = Gtk.FileChooserWidget(action=Gtk.FileChooserAction.OPEN)
box.pack_start(filechooserwidget, True, True, 0)

buttonbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)
buttonbox.set_layout(Gtk.ButtonBoxStyle.END)
buttonbox.set_spacing(2)
box.pack_start(buttonbox, False, False, 0)

button = Gtk.Button(label="_Open", use_underline=True)
button.connect("clicked", file_selected)
buttonbox.add(button)

window.show_all()

Gtk.main()