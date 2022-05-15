import tkinter as tk

from controllers.ExitController import ExitController
from controllers.ReadController import ReadController
from controllers.SaveConfigController import SaveConfigController
from controllers.SettingsController import SettingsController
from models.ReadModel import ReadModel
from models.SettingsModel import SettingsModel
from models.SaveConfigModel import SaveConfigModel
from models.ExitModel import ExitModel
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

        save_config_view = ReadView(self, "#0077B6", "Save config")
        save_config_model = SaveConfigModel()
        save_config_controller = SaveConfigController(save_config_model, save_config_view)
        save_config_view.set_controller(save_config_controller)

        exit_view = ReadView(self, "#EF476F", "Exit")
        exit_model = ExitModel()
        exit_controller = ExitController(exit_model, exit_view)
        exit_view.set_controller(exit_controller)

        read_view.grid(column=0, row=0)
        settings_view.grid(column=1, row=0)
        save_config_view.grid(column=2, row=0)
        exit_view.grid(column=3, row=0)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

