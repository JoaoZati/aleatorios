import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter oo')
        self.minsize(500, 400)
        self.columnconfigure(0, weight=1)

        self.create_label()
        self.button = self.create_button()

    def create_label(self):
        label_font = ('times', 40, 'bold')
        label = tk.Label(self, text='Text Label')
        label.config(font=label_font)
        label.grid(column=0, row=0)

    def create_button(self):
        button = ttk.Button(self, text = 'Click ME')
        button.grid(column=0, row=1)
        return button

window = Window()
window.mainloop()