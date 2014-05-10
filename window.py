#/usr/bin/env python3
  
from gi.repository import Gtk

window = Gtk.Window()
window.set_title("PyGObject Example")
window.connect("destroy", lambda q: Gtk.main_quit())
window.show()

Gtk.main()