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

    def add_conf_to_file(self):
        """
        Adds a configuration to 'conf.yaml' file.

        This method appends IMAP server, login, and password information to the 'conf.yaml' file.
        If a configuration for the given login already exists in the file, a message is printed and no
        changes are made. Otherwise, the configuration is added to the end of the file in YAML format.
        """
        imap, login, password = self.imap, self.login, self.password

        if self.is_config_present(login):
            print(f"Configuration for {login} already exists.")
            return

        with open('conf.yaml', 'a') as file:
            file.write('---\n')
            config_data = {'imap_server': imap, 'login': login, 'password': password}
            yaml.safe_dump(config_data, file, default_style="'")
            file.write('\n')

    @staticmethod
    def get_info_from_file():
        """
        Retrieves all configurations from 'conf.yaml' file.

        This method reads 'conf.yaml' file and extracts all configurations stored in it.
        Each configuration is added to a list, which is then returned.

        Returns:
            list: A list of dictionaries containing configuration data.
        """
        config_data_list = []
        with open('conf.yaml', 'r') as file:
            for config_data in yaml.safe_load_all(file):
                config_data_list.append(config_data)
        return config_data_list
