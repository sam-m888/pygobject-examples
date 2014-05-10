#!/usr/bin/env python3

from gi.repository import Gtk

def display_message_dialog(button, message_type):
    messagedialog = Gtk.MessageDialog(message_format="MessageDialog")
    messagedialog.set_property("message-type", message_type)
    
    messagedialog.run()
    messagedialog.destroy()

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

grid = Gtk.Grid()
grid.set_column_spacing(5)
window.add(grid)

buttonInfo = Gtk.Button(label="Information")
buttonInfo.connect("clicked", display_message_dialog, Gtk.MessageType.INFO)
grid.attach(buttonInfo, 0, 0, 1, 1)
buttonWarning = Gtk.Button(label="Warning")
buttonWarning.connect("clicked", display_message_dialog, Gtk.MessageType.WARNING)
grid.attach(buttonWarning, 1, 0, 1, 1)
buttonQuestion = Gtk.Button(label="Question")
buttonQuestion.connect("clicked", display_message_dialog, Gtk.MessageType.QUESTION)
grid.attach(buttonQuestion, 2, 0, 1, 1)
buttonError = Gtk.Button(label="Error")
buttonError.connect("clicked", display_message_dialog, Gtk.MessageType.ERROR)
grid.attach(buttonError, 3, 0, 1, 1)

window.show_all()

Gtk.main()