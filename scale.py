#!/usr/bin/env python

from gi.repository import Gtk
import random

def add_mark(button):
    value = scale.get_value()
    scale.add_mark(value, Gtk.PositionType.LEFT, "Mark")

def clear_marks(button):
    scale.clear_marks()

def scale_orientation(radiobutton):
	if radiobutton.get_label() == "Horizontal Scale":
		scale.set_orientation(Gtk.Orientation.HORIZONTAL)
	else:
		scale.set_orientation(Gtk.Orientation.VERTICAL)

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
window.add(grid)

value = random.randint(0, 100)
adjustment = Gtk.Adjustment(value, 0, 100, 1, 10, 0)

scale = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=adjustment)
scale.set_value_pos(Gtk.PositionType.BOTTOM)
scale.set_vexpand(True)
scale.set_hexpand(True)
grid.attach(scale, 0, 0, 2, 1)

buttonAdd = Gtk.Button(label="Add Mark")
buttonAdd.connect("clicked", add_mark)
grid.attach(buttonAdd, 0, 1, 1, 1)

buttonClear = Gtk.Button(label="Clear Marks")
buttonClear.connect("clicked", clear_marks)
grid.attach(buttonClear, 1, 1, 1, 1)

radiobuttonVertical = Gtk.RadioButton(group=None, label="Vertical Scale")
radiobuttonVertical.connect("toggled", scale_orientation)
grid.attach(radiobuttonVertical, 0, 3, 2, 1)

radiobuttonHorizontal = Gtk.RadioButton(group=radiobuttonVertical, label="Horizontal Scale")
radiobuttonHorizontal.connect("toggled", scale_orientation)
grid.attach(radiobuttonHorizontal, 0, 2, 2, 1)

window.show_all()

Gtk.main()