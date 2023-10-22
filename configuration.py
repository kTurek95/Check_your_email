import yaml


class Configuration:
    def __init__(self):
        self.imap = None
        self.login = None
        self.password = None

    def get_mail_conf(self, imap=None, login=None, password=None):
        if imap is None or login is None or password is None:
            self.imap = input('Podaj imap do swojej poczty: ')
            self.login = input('Podaj swój login: ')
            self.password = input('Podaj swoje hasło: ')
