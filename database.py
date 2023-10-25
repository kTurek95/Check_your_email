import email
from email.utils import parsedate_to_datetime
import sqlite3
from datetime import datetime


class Database:
    """
    A class to represent and manage an SQLite database connection.

    Attributes:
    file_name : str
        The name (or path) of the SQLite database file.
    cursor : sqlite3.Cursor or None
        The cursor object used to execute SQLite commands. Initialized to None until a connection is established.
    connection : sqlite3.Connection or None
        The connection object to the SQLite database. Initialized to None until a connection is established.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.cursor = None
        self.connection = None

    def create_login_information_table(self):
        """
        Creates the `login_information` table in the SQLite database if it doesn't exist.

        The `login_information` table consists of the following columns:
        - login_date: Textual representation of the login date.
        - email_id: A foreign key referencing the `id` column in the `emails` table.

        Also enables foreign key support in SQLite by setting "PRAGMA foreign_keys = ON;".
        """
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS login_information("
                            "login_date TEXT,"
                            "email_id INTEGER,"
                            "FOREIGN KEY(email_id) REFERENCES emails(id))")
        self.connection.commit()

    def create_emails_table(self):
        """
        Creates the `emails` table in the SQLite database if it doesn't exist.

        The `emails` table consists of the following columns:
        - id' - an auto-incremented primary key.
        - 'email' - a column to store email addresses as text.

        Also enables foreign key support in SQLite by setting "PRAGMA foreign_keys = ON;".
        """
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS emails("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "email TEXT)")
        self.connection.commit()

    def insert_into_emails_table(self, value, column_name):
        """
        Insert a new record into the 'emails' table in the SQLite database.

        Args:
        - value (str): The value to be inserted into the specified column.
        - column_name (str): The name of the column where the value should be inserted.

        This method checks if the email already exists in the database using the
        'email_exists' method. If the email does not exist, it inserts the new email
        into the 'emails' table. Otherwise, it does nothing.
        """
        if not self.email_exists(value):
            query = f"INSERT INTO emails ({column_name}) VALUES (?)"
            self.cursor.execute(query, value)
            self.connection.commit()

    def insert_into_login_table(self, login_date, email_id):
        """
        Inserts login information into the 'login_information' table.

        Args:
            login_date (str): The date of the login attempt.
            email_id (str): The email ID associated with the login attempt.

        Raises:
            sqlite3.Error: If there is an error while inserting data into the database.
        """
        if email_id:
            try:
                query = "INSERT INTO login_information (login_date, email_id) VALUES (?, ?)"
                self.cursor.execute(query, (login_date, email_id))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Error inserting into login_information: {e}")
