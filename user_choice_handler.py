from datetime import datetime
from database import Database

data = Database('database.db')


def menu():
    """
    Display a simple menu with options for the user.
    """
    print('---------- MENU ----------')
    print('1. Enter your email data and save it to a file')
    print('2. Display configuration from a file')
    print('3. Connect to email')
    print('4. Check email since last login')
    print('5. Exit')


def mail_connection(config, client):
    """
    Displays available email server configurations from a file and allows the user
    to select one of them. Upon selecting a configuration, the function establishes
    a connection to the email server and searches for messages.
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    configurations = config.get_info_from_file()

    for i, configuration in enumerate(configurations, start=1):
        print(f'{i}. {configuration["login"]}')

    user_config = int(input('Choose configuration: '))
    selected_config = configurations[user_config - 1]
    try:
        imap_server = client.connect_with_server(user_config)
        typ, _ = imap_server.select()
        if typ == 'OK':
            data.create_emails_table()
            data.insert_into_emails_table((selected_config['login'],), 'email')
            data.create_login_information_table()
            email_id = data.get_email_id(selected_config['login'])
            data.insert_into_login_table(login_date=formatted_time, email_id=email_id)
            client.search_messages(imap_server)
    except Exception as error:
        print(f'Error while connecting to the server: {error}')


def handle_user_choice(user_choice, config, client):
    """
    Handles the user's choice for various email-related operations.
    """
    data.create_emails_table()
    data.create_login_information_table()
    configurations = config.get_info_from_file()

    if user_choice == 1:
        config.get_mail_conf()
        config.add_conf_to_file()
    elif user_choice == 2:
        if len(configurations) == 0:
            print("You haven't added any configurations")
        else:
            print(configurations)
    elif user_choice == 3:
        if len(configurations) == 0:
            print("You haven't added any configurations")
        else:
            mail_connection(config, client)
    elif user_choice == 4:
        if len(configurations) == 0:
            print("You haven't added any configurations")
        else:
            i = 0
            for login_info in configurations:
                i += 1
                print(f'{i}. {login_info["login"]}')
            try:
                new_msg = data.get_new_emails_since_last_login(client)
                if len(new_msg) > 0:
                    for msg in new_msg:
                        msg_info = f' From: {msg["FROM"]}, Subject: {msg["SUBJECT"]}'
                        print(msg_info)
                else:
                    print('You have no new messages')
            except TypeError:
                print("You don't have any data in the database")
    elif user_choice == 5:
        return False
    return True
