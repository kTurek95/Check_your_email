import imaplib
from database import Database


class EmailClient:
    """
    A client to handle interactions with email servers
    """
    def __init__(self, configurations, file_name):
        """
        Initializes the EmailClient with the provided configurations and file name.

        Args:
            configurations (list): A list of configurations for different email servers.
            file_name (str): Name of the file to be used by the Database instance.
        """
        self.configurations = configurations
        self.file_name = file_name
        self.database = Database(file_name)

    def connect_with_server(self, user_choice):
        """
        Connects to the email server specified by the user's choice.

        Args:
            user_choice (int): Index of the user's chosen configuration (1-based index).

        Returns:
            IMAP4_SSL: An instance of IMAP4_SSL representing the email server connection.

        Raises:
            IMAP4.error: If there's an error while connecting or authenticating to the server.
        """
        config = self.configurations[user_choice - 1]
        imap_server = imaplib.IMAP4_SSL(host=config['imap_server'])
        imap_server.login(config['login'], config['password'])
        return imap_server
