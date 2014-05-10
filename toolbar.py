#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(500, -1)
window.connect("destroy", lambda q: Gtk.main_quit())

toolbar = Gtk.Toolbar()
window.add(toolbar)

toolbutton = Gtk.ToolButton(stock_id=Gtk.STOCK_NEW)
toolbutton.set_is_important(True)
toolbar.add(toolbutton)

toggletoolbutton = Gtk.ToggleToolButton(stock_id=Gtk.STOCK_MEDIA_PLAY)
toolbar.add(toggletoolbutton)

menu = Gtk.Menu()
menuitem = Gtk.MenuItem(label="MenuItem")
menu.append(menuitem)

menutoolbutton = Gtk.MenuToolButton(stock_id=Gtk.STOCK_OPEN)
menutoolbutton.set_menu(menu)
toolbar.add(menutoolbutton)

separatortoolitem = Gtk.SeparatorToolItem()
toolbar.add(separatortoolitem)

radiotoolbutton1 = Gtk.RadioToolButton(group=None, stock_id=Gtk.STOCK_MEDIA_REWIND)
toolbar.add(radiotoolbutton1)
radiotoolbutton2 = Gtk.RadioToolButton(group=radiotoolbutton1, stock_id=Gtk.STOCK_MEDIA_FORWARD)
toolbar.add(radiotoolbutton2)

separatortoolitem = Gtk.SeparatorToolItem()
toolbar.add(separatortoolitem)

toolitem = Gtk.ToolItem()
entry = Gtk.Entry()
toolitem.add(entry)
toolbar.add(toolitem)

menuitem.show()
window.show_all()

Gtk.main()