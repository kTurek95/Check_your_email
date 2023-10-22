import yaml


class Configuration:
    def __init__(self):
        self.imap = None
        self.login = None
        self.password = None

    def get_mail_conf(self, imap=None, login=None, password=None):
        """
        Fetches and sets the mail configuration for the instance.

        If any of the parameters (imap, login, password) are not provided,
        it prompts the user to enter the missing values interactively.

        Parameters:
        - imap (str, optional): The IMAP server address. If not provided, the user will be prompted.
        - login (str, optional): The login/email for the mail account. If not provided, the user will be prompted.
        - password (str, optional): The password for the mail account. If not provided, the user will be prompted.

        Returns:
        None
        """
        if imap is None or login is None or password is None:
            self.imap = input('Enter the IMAP for your mail: ')
            self.login = input('Enter your login: ')
            self.password = input('Enter your password: ')

    @staticmethod
    def is_config_present(new_login):
        """
        Checks if a given configuration, based on login, is already present in the 'conf.yaml' file.

        Args:
            new_login (str): The login string to be checked against existing configurations.

        Returns:
            bool: True if the login configuration is already present, otherwise False.

        """
        with open('conf.yaml', 'r') as file:
            for line in file:
                config_data = yaml.safe_load(line)
                if config_data is not None and config_data.get('login') == new_login:
                    return True
        return False
