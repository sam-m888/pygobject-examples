#!/usr/bin/env python3
import os
from gi.repository import Gtk, Gdk

class TextEditor(Gtk.Window):

    def keyboard_shortcuts(self, widget):
        window = Gtk.Window()
        window.set_title("Keyboard shortcuts")
        window.set_default_size(200, -1)
        window.set_border_width(6)
        window.connect("destroy", lambda q: Gtk.main_quit())
        window.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        window.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 0, 1))
        label = Gtk.Label(label="CTRL + S = Save this post\nCTRL + O = Open File\nCTRL + N = New file\nCTRL + H = About\nCTRL + Q = Quit\nCTRL + D = Delete this post")
        window.add(label)
        window.show_all()
        Gtk.main()

    def new_win(self, widget):
        win = TextEditor()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def choose_file(self, widget):
        chooser_dialog = Gtk.FileChooserDialog(title="Select file"
        ,action=Gtk.FileChooserAction.OPEN
        ,buttons=["OK", Gtk.ResponseType.OK, "Cancel", Gtk.ResponseType.CANCEL])
        filter_pdf = Gtk.FileFilter()
        filter_pdf.set_name("All files")
        filter_pdf.add_pattern("*")
        chooser_dialog.add_filter(filter_pdf)
        chooser_dialog.run()
        filename = chooser_dialog.get_filename()
        if filename is not None:
            with open(filename) as read_title_and_date:
                for i, line in enumerate(read_title_and_date.readlines(), 0):
                    for char in line:
                        if char in ("\n", "#"):
                            line = line.replace(char,'')
                    if i == 0:
                        self.entry_title.set_text(line[1:-1])
                    if i == 2:
                        self.entry_date.set_text(line)
            with open(filename) as read_text:
                self.textbuffer.set_text("{0}".format(read_text.read()))
                cur_dir = os.getcwd()
                batman, md_post_name = os.path.split(cur_dir + "/{0}".format(filename))
                self.entry_name.set_text(md_post_name)
                read_text.close()
        chooser_dialog.destroy()

    def delete_this_post(self, widget):
        os.remove("{0}".format(self.entry_name.get_text()))

    def about_dialog(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_logo_icon_name(Gtk.STOCK_ABOUT)
        aboutdialog.set_program_name("Text Editor Pro")
        aboutdialog.set_comments("\nSimple text editor\n")
        aboutdialog.set_website("http://mywebsite.com/")
        aboutdialog.set_website_label("Some Label")
        aboutdialog.set_authors(["Unknown Author", ""])
        aboutdialog.set_license("""License:\nFree to use""")
        aboutdialog.run()
        aboutdialog.destroy()

    def toolbar(self):
        self.accelgroup = Gtk.AccelGroup()
        self.add_accel_group(self.accelgroup)

        toolbar = Gtk.Toolbar()
        toolbar.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        self.grid.attach(toolbar, 0, 0, 3, 1)

        action_new_file = Gtk.ToolButton(Gtk.STOCK_NEW)
        action_new_file.set_tooltip_text("New File")
        action_save = Gtk.ToolButton(Gtk.STOCK_SAVE)
        action_save.set_tooltip_text("Save this post")
        action_quit = Gtk.ToolButton(Gtk.STOCK_QUIT)
        action_quit.set_tooltip_text("Quit")
        action_about = Gtk.ToolButton(Gtk.STOCK_ABOUT)
        action_about.set_tooltip_text("About Text Editor Pro")
        action_delete_this_post = Gtk.ToolButton(Gtk.STOCK_DELETE)
        action_delete_this_post.set_tooltip_text("Delete This post")
        action_choose_file = Gtk.ToolButton(Gtk.STOCK_OPEN)
        action_choose_file.set_tooltip_text("Open File")
        action_usage = Gtk.ToolButton(Gtk.STOCK_DIALOG_QUESTION)
        action_usage.set_tooltip_text("Keyboard shortcuts")

        toolbar.insert(action_new_file, 0)
        toolbar.insert(action_choose_file, 1)
        toolbar.insert(action_save, 2)
        toolbar.insert(action_about, 3)
        toolbar.insert(action_usage, 4)
        toolbar.insert(action_quit, 5)
        toolbar.insert(Gtk.SeparatorToolItem(), 6)
        toolbar.insert(action_delete_this_post, 7)
        toolbar.insert(Gtk.SeparatorToolItem(), 8)

        action_new_file.connect("clicked", self.new_win)
        action_quit.connect("clicked", Gtk.main_quit)
        action_about.connect("clicked", self.about_dialog)
        action_save.connect("clicked", self.save_text)
        action_delete_this_post.connect("clicked", self.delete_this_post)
        action_choose_file.connect("clicked", self.choose_file)
        action_usage.connect("clicked", self.keyboard_shortcuts)

        action_choose_file.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("o"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        action_new_file.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("n"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        action_quit.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("q"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        action_about.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("h"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        action_delete_this_post.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("d"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
        action_save.add_accelerator("clicked", self.accelgroup, Gdk.keyval_from_name("s"), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)

    def text_field(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("")
        scrolledwindow.add(self.textview)

    def save_text(self, widget):
        cur_dir = os.getcwd()
        f = open(cur_dir + "/{0}".format(self.entry_name.get_text()), "wt")
        f.write("# {0} #\n".format(self.entry_title.get_text()))
        f.write('empty line\n')
        f.write("{0}\n".format(self.entry_date.get_text()))
        f.write('empty line 2\n\n')
        f.write(self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True))
        f.close()

    def __init__(self):
        Gtk.Window.__init__(self, title="Text Editor")

        self.set_default_size(550, 400)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.entry_title = Gtk.Entry()
        self.entry_title.set_width_chars(1)
        self.entry_title.set_text("File Title")
        self.entry_title.set_max_length(46)
        self.grid.attach(self.entry_title, Gtk.PositionType.LEFT, 2, 1, 1)

        self.entry_name = Gtk.Entry()
        self.entry_name.set_width_chars(1)
        self.entry_name.set_text("file_name")
        self.entry_name.set_max_length(33)
        self.grid.attach(self.entry_name, Gtk.PositionType.RIGHT, 2, 1, 1)

        self.entry_date = Gtk.Entry()
        self.entry_date.set_width_chars(1)
        self.entry_date.set_text("2014-05-10")
        self.entry_date.set_max_length(10)
        self.grid.attach(self.entry_date, 2, 2, 1, 1)

        self.text_field()
        self.toolbar()

if __name__ == '__main__':
    win = TextEditor()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()