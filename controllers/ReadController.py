from services.SSHConnection import SSHConnection


class ReadController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.conf = None

    def open_view(self):
        """ Connect to cisco server"""
        ssh_connection = SSHConnection()
        con = ssh_connection.conn()

        # TODO
        # Set the view to show that application are connected
