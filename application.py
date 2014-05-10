#!/usr/bin/env python3

from gi.repository import Gtk, Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
	def __init__(self, app):
		Gtk.Window.__init__(self, title="Menubutton Example", application=app)
		self.set_default_size(600, 400)
		
		grid = Gtk.Grid()
		
		menubutton = Gtk.MenuButton()
		menubutton.set_size_request(80, 35)
		grid.attach(menubutton, 0, 0, 1, 1)
		
		menumodel = Gio.Menu()
		menubutton.set_menu_model(menumodel)
		menumodel.append("New", "app.new")
		menumodel.append("Quit", "app.quit")
		
		self.add(grid)

class MyApplication(Gtk.Application):
	def __init__(self):
		Gtk.Application.__init__(self)

	def do_activate(self):
		win = MyWindow(self)
		win.show_all()

	def do_startup(self):
		Gtk.Application.do_startup(self)

		new_action = Gio.SimpleAction.new("new", None)
		new_action.connect("activate", self.new_callback)
		self.add_action(new_action)

		quit_action = Gio.SimpleAction.new("quit", None)
		quit_action.connect("activate", self.quit_callback)
		self.add_action(quit_action)

	def new_callback(self, action, parameter):
		print("You clicked \"New\"")

	def quit_callback(self, action, parameter):
		print("You clicked \"Quit\"")
		self.quit()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)