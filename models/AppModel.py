class AppModel:
    def __init__(self):
        self.read_model = None
        self.settings_model = None

    @property
    def read(self):
        return self.__read_model

    @property
    def settings(self):
        return self.__settings_model

    @read.setter
    def read(self, value):
        """
        add instance of read model
        :param value:
        :return:
        """
        self.__read_model = value

    @settings.setter
    def settings(self, value):
        """
        add instance for settings model
        :param value:
        :return:
        """
        self.__settings_model = value
