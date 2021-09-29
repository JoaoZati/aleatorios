import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter oo')
        self.minsize(500, 400)
        self.columnconfigure(0, weight=1)

        self.create_label()

    def create_label(self):
        label_font = ('times', 40, 'bold')
        label = tk.Label(self, text='Text Label')
        label.config(font=label_font)
        label.grid(column=0, row=0)

window = Window()
window.mainloop()