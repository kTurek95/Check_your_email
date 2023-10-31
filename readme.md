# Check your email

The program is used for checking mail. The user can add as many configurations as they want and keep them in one place. They can also check how many messages they have in a particular mailbox, see if there are any messages since the last login, and much more.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running:
- pip install -r requirements.txt

## Usage

1. Run the **main.py** script to interact with program - python main.py (**on windows and macOS**).
2. If you don't have an env file created, you can create it manually by adding it to the repository folder. Alternatively, upon launching the program, it will ask for a password and create the env file with the provided password.
3. Run the **main.py** script again and add email configuration by using option 1. The configurations will be stored in the conf.yaml file
4. Then run the **main.py** script one more time and choose the option you would like to execute.
5. If you would like to exit the program choose option 5. 

## Modules

#### main.py
The main module contains the main function responsible for the program's logic, as well as the create_env_file function, which creates the env file.
#### emailclient.py
Module responsible for connecting and interacting with email containing the EmailClient class.
#### database.py
Module responsible for creating and connecting to the database, containing the Database class.
#### user_choice_handler.py
A module that has a menu function displaying program options to the user, a mail_connection function responsible for checking the connection with the email, and a handle_user_choice function that handles the user's selections.
#### configuration.py
Module responsible for retrieving email configuration from the user and saving it in the conf.yaml file, containing the Configuration class.

## Support

If you encounter any issues with my software, please reach out to me:
- Email: k.turek1995@gmail.com

## Dependencies
To run this software, you'll need the libraries and tools listed in requirements.txt

## License
This project is licensed under the MIT License - 
[![Licencja MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)