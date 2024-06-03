# pip install mysql connector - latest version
from flask import Flask, render_template, request
import mysql.connector  # imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import Error
# import the Error class from mysql.connector module to handle exceptions that occur while interacting with the MySQL database
# this will handle database errors - when error occurs i.e. connection failure or syntax error the 'Error' exception will be raised
import logging  # import logging module to log errors if raised

logging.basicConfig(filename='app.log', level=logging.DEBUG)  # Set to DEBUG to capture more detailed logs

class DatabaseInsertionError(Exception):
    def __init__(self, message):
        super().__init__(message)  # custom exception handling class for database insertion error


class DatabaseConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)  # custom exception handling class for connection error


app = Flask(__name__)

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            logging.debug("Connected to the database")
            return self.connection
        except Error as error:
            logging.error(f"The server could not connect to MySQL due to {error}")
            raise DatabaseConnectionError("Could not connect to the database")

    def close(self):
        if self.connection:
            self.connection.close()
            logging.debug("Database connection closed")

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            logging.debug("Creating tables...")
            create_users_table = """
                CREATE TABLE IF NOT EXISTS users_table (
                    user_id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR(225) NOT NULL,
                    email VARCHAR(100) NOT NULL
                )
            """
            create_locations_table = """
                CREATE TABLE IF NOT EXISTS Locations (
                    location_id VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    type VARCHAR(50),
                    address VARCHAR(255),
                    city VARCHAR(100),
                    post_code VARCHAR(15),
                    phone_number VARCHAR(20),
                    rating DECIMAL(3, 2),
                    image_url VARCHAR(255),
                    yelp_url VARCHAR(255),
                    latitude DECIMAL(9,5),
                    longitude DECIMAL(9,5)
                )
            """
            create_search_history_table = """
                CREATE TABLE IF NOT EXISTS Search_History (
                    search_id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    searched_location VARCHAR(255),
                    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    results JSON,
                    FOREIGN KEY (user_id) REFERENCES users_table (user_id)
                )
            """
            create_contact_form_table = """
                CREATE TABLE IF NOT EXISTS contact_form (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            cursor.execute(create_users_table)
            cursor.execute(create_locations_table)
            cursor.execute(create_search_history_table)
            cursor.execute(create_contact_form_table)
            self.connection.commit()
            logging.info("Tables created successfully")
        except Error as error:
            logging.error(f"The following error occurred when creating the tables: {error}")
            raise DatabaseInsertionError("The location information could not be saved")
        finally:
            if cursor:
                cursor.close()
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="newuser",
            password="new_password",
            database="pet_friendly_database"
        )
        logging.debug("Database connection established")
        return connection
    except Error as error:
        logging.error(f"There was an error connecting to MySQL: {error}")
        return None

def main():
    connection = get_db_connection()
    if connection:
        db = Database(host="localhost", user="newuser", password="new_password", database="pet_friendly_database")
        db.connect()
        db.create_tables()
        db.close()
        print('done')
    else:
        logging.error("Error connecting to the database")

if __name__ == "__main__":
    main()
