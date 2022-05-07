import tkinter as tk

from controllers.ReadController import ReadController
from controllers.SettingsController import SettingsController
from models.ReadModel import ReadModel
from models.SettingsModel import SettingsModel
from views.ReadView import ReadView


class AppView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.config(background="#4c283c", width="450", height="300", padx=10, pady=10)

        read_view = ReadView(self, "#d1a284", 'Read')
        read_model = ReadModel()
        read_controller = ReadController(read_model, read_view)
        read_view.set_controller(read_controller)

        settings_view = ReadView(self, "#545470", 'Settings')
        settings_model = SettingsModel()
        settings_controller = SettingsController(settings_model, settings_view)
        settings_view.set_controller(settings_controller)

        read_view.grid(column=0, row=0)
        settings_view.grid(column=1, row=0)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

