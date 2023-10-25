import sqlite3


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
