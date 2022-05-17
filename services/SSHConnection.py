from netmiko import ConnectHandler, BaseConnection
import json


class SSHConnection:
    config_file = "config.json"

    def __init__(self):
        self._cli: BaseConnection = None

    @property
    def conn(self):
        if not self._cli:
            self._cli = self._get_connection()
        return self._cli

    @staticmethod
    def load_config():
        with open(SSHConnection.config_file) as file:
            return json.load(file)

    @staticmethod
    def _get_connection():
        return ConnectHandler(**SSHConnection.load_config())
