import sqlite3
import os

class DBConnector:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")

    def get_cursor(self):
        """Return a cursor from the active connection."""
        if not self.connection:
            raise ConnectionError("No active database connection. Call connect() first.")
        return self.connection.cursor()
    
    def commit(self):
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
            self.connection = None
        else:
            print("No database connection to close.")