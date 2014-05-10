#!/usr/bin/env python3

from gi.repository import Gtk

def comboboxtext_changed(comboboxtext):
	print(comboboxtext.get_active_text())

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

comboboxtext = Gtk.ComboBoxText()
comboboxtext.append("gnome", "GNOME")
comboboxtext.append("kde", "KDE")
comboboxtext.append("xfce", "XFCE")
comboboxtext.append("lxde", "LXDE")
comboboxtext.set_active(0)
comboboxtext.connect("changed", comboboxtext_changed)
window.add(comboboxtext)

window.show_all()

Gtk.main()