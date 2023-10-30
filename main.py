import os.path
import time
from os import getenv
import click
from dotenv import load_dotenv
from configuration import Configuration
from emailclient import EmailClient
from user_choice_handler import menu, handle_user_choice


def create_env_file(password):
    try:
        with open(".env", "w") as env_file:
            env_file.write(f'PASSWORD={password}')
        print('The env file with password has been successfully created')
    except Exception as e:
        print(f'An error occurred while creating the env file: {e}')


def main():
    config = Configuration()
    client = EmailClient(config.get_info_from_file(), 'database.db')
    load_dotenv()
    password = getenv('PASSWORD')
    counter = 3
    if not os.path.exists('.env'):
        user_password = click.prompt('Enter the password that will be set as the main password', hide_input=True)
        create_env_file(user_password)
    else:
        user_password = click.prompt('Enter password', hide_input=True)
        while True:
            if user_password == password:
                menu()
                user_choice = int(input('Choose what you want to do: '))

                if not handle_user_choice(user_choice, config, client):
                    print('You have exited the program')
                    break
            else:
                counter -= 1
                print('You entered the wrong password. There have been attempts: ', counter)
                user_password = click.prompt('Enter password', hide_input=True)
                if counter == 0:
                    print('Access to the program is blocked for 30 seconds')
                    time.sleep(30)
                    counter = 3


if __name__ == '__main__':
    main()
