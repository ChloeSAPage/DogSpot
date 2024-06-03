# pip install mysql connector - latest version
from flask import Flask, render_template, request
import mysql.connector  # imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import Error
# import the Error class from mysql.connector module to handle exceptions that occur while interacting with the MySQL database
# this will handle database errors - when error occurs i.e. connection failure or syntax error the 'Error' exception will be raised
import logging  # import logging module to log errors if raised

logging.basicConfig(filename='app.log', level=logging.ERROR)

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
            return self.connection
        except Error as error:
            logging.error(f"The server could not connect to MySQL due to {error}")
            raise DatabaseConnectionError("Could not connect to the database")

    def close(self):
        if self.connection:
            self.connection.close()

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
                # Insert SQL statements to create the tables
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
            cursor.execute(create_users_table)
            cursor.execute(create_search_history_table)
            cursor.execute(create_locations_table)

                # note: maybe add logging.ingo here to confirm tables created successfully unless error raised
            logging.info("Tables created successfully")
        except Error as error:
            logging.error(f"The following error occurred when creating the tables {error}")
                # this doesn't directly take the users input so what kind of error can be raised?
            raise DatabaseInsertionError("The location information could not be saved")
        finally:
            cursor.close()

    def insert_location(self, location_data):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO Locations
            (location_id, name, type, address, city, post_code, phone_number, rating, image_url, yelp_url, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, location_data)
            self.connection.commit()  # save the inserted info permanently into the database
            logging.info("The location data was successfully stored")
        except mysql.connector.Error as error:
            logging.error(f"The location data could not be inserted due to {error} error")
            raise DatabaseInsertionError("There was an error inserting the data")
        finally:
            if cursor:
                cursor.close()  # check if the cursor is not none then close. prevents memory leaks

class UserSignup:
    def __init__(self, db):
        self.db = db
    def register_user(self):
        connection = self.db.connect()
        if connection:
            try:
                email = request.form["email"]
                username = request.form["username"]
                password = request.form["password"]

                if not email or not username or not password:
                    raise ValueError("All fields must be filled out")

                cursor = connection.cursor()
                query = "INSERT INTO users_table (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(query, (username, password, email))
                connection.commit()
                cursor.close()
                logging.info("User signup details have successfully been stored in the database")
            except mysql.connector.Error as error:
                logging.error(f"The user details could not be inserted into the database due to: {error}")
                raise DatabaseInsertionError("There was an error storing the users info")
            finally:
                connection.close()
        else:
            logging.error("Connection not established")
            raise DatabaseConnectionError("Error connecting to the database")

# def register_user(username, password):
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="your_username",
#             password="your_password",
#             database="your_database"
#         )
#         return connection
#     except mysql.connector.Error as error:
#         print(f"The server could not connect to MySQL due to {error}")


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pet_friendly_database"
        )
        return connection
    except Error as error:
        logging.error(f"There was an error connecting to MySQL: {error}")  # log this error so not printed to the user
        return None


def create_tables(connection):
    try:
        cursor = self.connection.cursor()
        # Insert SQL statements to create the tables
        create_users_table = """
            CREATE TABLE IF NOT EXISTS users_table (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
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
                latitude DECIMAL(9,9),
                longitude DECIMAL(9,9)
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
        cursor.execute(create_users_table)
        cursor.execute(create_search_history_table)
        cursor.execute(create_locations_table)

        # note: maybe add logging.ingo here to confirm tables created successfully unless error raised
        logging.info("Tables created successfully")
    except Error as error:
        logging.error(f"The following error occurred when creating the tables {error}")
        # this doesn't directly take the users input so what kind of error can be raised?
        raise DatabaseInsertionError("The location information could not be saved")
    finally:
        cursor.close()


@app.route("/")
def signup_form():
    return render_template("")   # insert html for signup form to call this function when user accesses the form
@app.route("/", methods=["POST"])
def signup():
    db = Database(host="localhost", user="root", password="", database="pet_friendly_database")
    user_signup = UserSignup(db)
    try:
        user_signup.register_user()
        return "User details stored successfuly"
    except:
        raise DatabaseInsertionError("Could not store user info")


# insert data into database
def insert_location(connection, location_info):
    cursor = None  # initialise cursor before the try/except block - set to None to avoid error
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Locations
        (location_id, name, type, address, city, post_code, phone_number, rating, image_url, yelp_url, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, location_info)
        connection.commit()  # save the inserted info permanently into the database
        logging.info("The location data was successfully stored")
    except mysql.connector.Error as error:
        logging.error(f"The location data could not be inserted due to {error} error")
        raise DatabaseInsertionError("The location could not be stored in the database")
        # could add raise here
    finally:
        if cursor:
            cursor.close()  # check if the cursor is not none then close. prevents memory leaks


# Main function - connect to database and create the tables


def main():
    db = Database(host="localhost", user="root", password="", database="pet_friendly_database")
    try:
        connection = db.connect()
        if connection:
            db.create_tables()
        else:
            raise DatabaseConnectionError("There was an error connecting to the database")
    except (DatabaseInsertionError, DatabaseConnectionError) as error:
        logging.error(f"An error occurred: {error}")



if __name__ == "__main__":
    main()