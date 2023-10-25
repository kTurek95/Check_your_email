import email
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

    @staticmethod
    def select_mailbox(imap_server):
        """
        Allows the user to select a mailbox (e.g. inbox, sent, drafts) and attempts to select it on the given IMAP server.

        Parameters:
        - imap_server (object): The IMAP server connection object.

        Returns:
        - bool: True if the mailbox selection was successful, False otherwise.
        """
        print('inbox, sent, drafts, trash, spam')
        mail_option = input('Choose which mailbox you want to check: ')
        try:
            imap_server.select(mail_option)
            return True
        except imaplib.IMAP4.error as error:
            print(f'An IMAP4 error occurred: {error}')
            return False

    @staticmethod
    def search_by_sender(imap_server):
        """
        Allows the user to search for emails based on sender-related criteria on the given IMAP server.

        Parameters:
        - imap_server (object): The IMAP server connection object.

        Note:
        - Currently supported search criteria are 'all', 'seen', and 'unseen'.
        """
        print('all, seen, unseen')
        user_option = input('Choose a search option: ')
        status, messages = imap_server.search(None, user_option)
        message_ids = messages[0].split()
        for message_id in message_ids:
            status, msg_data = imap_server.fetch(message_id, '(BODY[HEADER.FIELDS (FROM SUBJECT)])')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            from_address = msg['From']
            print(f'Sender: {from_address}')

    @staticmethod
    def search_by_subject(imap_server):
        """
       Allows the user to search for emails based on given criteria and displays the subject of matched emails
       on the provided IMAP server.

       Parameters:
       - imap_server (object): The IMAP server connection object.
        """
        print('all, seen, unseen')
        user_option = input('Choose a search option.: ')
        status, messages = imap_server.search(None, user_option)
        message_ids = messages[0].split()
        for message_id in message_ids:
            status, msg_data = imap_server.fetch(message_id, '(BODY[HEADER.FIELDS (FROM SUBJECT)])')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = msg['Subject']
            print('Subject: ', subject)

    def search_messages(self, imap_server):
        """
        Allows the user to search for messages in a selected mailbox based on various criteria,
        including by sender and subject.

        The function first prompts the user to select a mailbox. If the mailbox selection
        is successful, the user can then choose from a list of search criteria. Depending
        on the choice, the function delegates the search to dedicated methods or directly
        performs the search on the provided IMAP server.

        Parameters:
        - imap_server (object): The IMAP server connection object.
        """
        if self.select_mailbox(imap_server):
            print('all, unseen, seen, email sender, email subject ')
            search_options = input('Wybierz opcje wyszukiwania: ')
            if search_options == 'email sender':
                self.search_by_sender(imap_server)
            elif search_options == 'email subject':
                self.search_by_subject(imap_server)
            else:
                status, messages = imap_server.search(None, search_options)
                print(messages)
