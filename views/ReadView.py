import tkinter as tk
from functools import partial


class ReadView(tk.Frame):
    def __init__(self, parent, color, title):
        super().__init__(parent)

        self.config(background=color, width="150", height="150", padx=20, pady=20)

        button = tk.Button(self, text=title, command=self.open_view)

        button.grid()

        self.controller = None

    def open_view(self):
        self.controller.open_view()

    def set_controller(self, controller):
        self.controller = controller
