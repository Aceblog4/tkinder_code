import tkinter as tk

from controllers.AppController import AppController
from models.AppModel import AppModel
from views.AppView import AppView


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cisco AI")

        self.config(background="#4c283c")

        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.geometry('500x100+%d+%d' % (x, y))

        # create a model
        model = AppModel()

        # create a view and place it on the root window
        view = AppView(self)
        view.grid(row=0, column=0)

        # create a controller
        controller = AppController(model, view)

        view.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
