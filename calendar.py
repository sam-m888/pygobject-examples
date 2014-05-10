#!/usr/bin/env python3

from gi.repository import Gtk

def calendar_change(checkbutton, option):
    display_options = []
    
    if checkbutton.get_active():
        display_options.append(option)
    
    calendar.set_display_options(Gtk.CalendarDisplayOptions.SHOW_HEADING)

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
window.add(hbox)

calendar = Gtk.Calendar()
hbox.pack_start(calendar, True, True, 0)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
hbox.pack_start(vbox, False, False, 0)

checkbutton_heading = Gtk.CheckButton(label="Show heading")
checkbutton_heading.connect("toggled", calendar_change, Gtk.CalendarDisplayOptions.SHOW_HEADING)
vbox.pack_start(checkbutton_heading, False, False, 0)

checkbutton_daynames = Gtk.CheckButton(label="Show day names")
checkbutton_daynames.connect("toggled", calendar_change, Gtk.CalendarDisplayOptions.SHOW_DAY_NAMES)
vbox.pack_start(checkbutton_daynames, False, False, 0)

checkbutton_preventchange = Gtk.CheckButton(label="Prevent month/year change")
checkbutton_preventchange.connect("toggled", calendar_change)
vbox.pack_start(checkbutton_preventchange, False, False, 0)

checkbutton_weeknumbers = Gtk.CheckButton(label="Show week numbers")
checkbutton_weeknumbers.connect("toggled", calendar_change)
vbox.pack_start(checkbutton_weeknumbers, False, False, 0)

window.show_all()

Gtk.main()