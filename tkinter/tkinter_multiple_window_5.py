import tkinter as tk  # import Tkinter as tk #change to commented for python2

dialog_window = None


def create_dialog():
    """creates the dialog window
  ** do not call if dialog_window is already open, this will
     create a duplicate without handling the other
if you are unsure if it already exists or not use show_dialog()"""
    global dialog_window
    dialog_window = tk.Toplevel(root)
    label1 = tk.Label(dialog_window, text="this is the dialog window")
    label1.pack()
    # put other widgets
    dialog_window.lift()  # ensure it appears above all others, probably will do this anyway


def show_dialog():
    """lifts the dialog_window if it exists or creates a new one otherwise"""
    # this can be refactored to only have one call to create_dialog()
    # but sometimes extra code will be wanted the first time it is created
    if dialog_window is None:
        create_dialog()
        return
    try:
        dialog_window.lift()
    except tk.TclError:
        # window was closed, create a new one.
        create_dialog()


root = tk.Tk()

dialog_button = tk.Button(root,
                          text="show dialog_window",
                          command=show_dialog)
dialog_button.pack()
root.mainloop()