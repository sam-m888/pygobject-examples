#!/usr/bin/env python3

from gi.repository import Gtk

def apply_button_clicked(assistant):
    print("The 'Apply' button has been clicked")

def close_button_clicked(assistant):
    print("The 'Close' button has been clicked")
    Gtk.main_quit()

def cancel_button_clicked(assistant):
    print("The 'Cancel' button has been clicked")
    Gtk.main_quit()

def checkbutton_toggled(checkbutton):
    assistant.set_page_complete(box1, checkbutton.get_active())

assistant = Gtk.Assistant()
assistant.connect("cancel", cancel_button_clicked)
assistant.connect("close", close_button_clicked)
assistant.connect("apply", apply_button_clicked)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
assistant.append_page(box)
assistant.set_page_type(box, Gtk.AssistantPageType.INTRO)
assistant.set_page_title(box, "Page 1: Introduction")
label = Gtk.Label(label="An 'Intro' page is the first page of an Assistant. It is used to provide information about what configuration settings need to be configured. The introduction page only has a 'Continue' button.")
label.set_line_wrap(True)
box.pack_start(label, True, True, 0)
assistant.set_page_complete(box, True)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
assistant.append_page(box)
assistant.set_page_type(box, Gtk.AssistantPageType.CONTENT)
assistant.set_page_title(box, "Page 2: Content")
label = Gtk.Label(label="The 'Content' page provides a place where widgets can be positioned. This allows the user to configure a variety of options as needed. The page contains a 'Continue' button to move onto other pages, and a 'Go Back' button to return to the previous page if necessary.")
label.set_line_wrap(True)
box.pack_start(label, True, True, 0)
assistant.set_page_complete(box, True)

box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
age = assistant.append_page(box1)
assistant.set_page_type(box1, Gtk.AssistantPageType.PROGRESS)
assistant.set_page_title(box1, "Page 3: Progress")
label = Gtk.Label(label="A 'Progress' page is used to prevent changing pages within the Assistant before a long-running process has completed. The 'Continue' button will be marked as insensitive until the process has finished. Once finished, the button will become sensitive.")
label.set_line_wrap(True)
box1.pack_start(label, True, True, 0)
checkbutton = Gtk.CheckButton(label="Mark page as complete")
checkbutton.connect("toggled", checkbutton_toggled)
box1.pack_start(checkbutton, False, False, 0)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
assistant.append_page(box)
assistant.set_page_type(box, Gtk.AssistantPageType.CONFIRM)
assistant.set_page_title(box, "Page 4: Confirm")
label = Gtk.Label(label="The 'Confirm' page may be set as the final page in the Assistant, however this depends on what the Assistant does. This page provides an 'Apply' button to explicitly set the changes, or a 'Go Back' button to correct any mistakes.")
label.set_line_wrap(True)
box.pack_start(label, True, True, 0)
assistant.set_page_complete(box, True)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
assistant.append_page(box)
assistant.set_page_type(box, Gtk.AssistantPageType.SUMMARY)
assistant.set_page_title(box, "Page 5: Summary")
label = Gtk.Label(label="A 'Summary' should be set as the final page of the Assistant if used however this depends on the purpose of your Assistant. It provides information on the changes that have been made during the configuration or details of what the user should do next. On this page only a Close button is displayed. Once at the Summary page, the user cannot return to any other page.")
label.set_line_wrap(True)
box.pack_start(label, True, True, 0)
assistant.set_page_complete(box, True)

assistant.show_all()

Gtk.main()