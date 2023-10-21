def menu():
    """
    Display a simple menu with options for the user.
    """
    print('---------- MENU ----------')
    print('1. Enter your email data and save it to a file')
    print('2. Display configuration from a file')
    print('3. Connect to email')
    print('4. Exit')


def mail_connection(config, client):
    """
    Displays available email server configurations from a file and allows the user
    to select one of them. Upon selecting a configuration, the function establishes
    a connection to the email server and searches for messages.
    """
    i = 1
    for configuration in config.get_info_from_file():
        print(f'{i}. {configuration}')
        i += 1
    user_config = int(input('Wybierz konfigurację: '))
    imap_server = client.connect_with_server(user_config)
    client.search_messages(imap_server)
