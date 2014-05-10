#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(300, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

notebook = Gtk.Notebook()
window.add(notebook)

for page in range(1, 4):
    label1 = Gtk.Label(label="Notebook")
    label2 = Gtk.Label()
    label2.set_text("Page %s" % str(page))
    notebook.append_page(label1, label2)
    notebook.set_tab_reorderable(label1, True)

window.show_all()

Gtk.main()