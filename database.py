# pip install mysql connector - latest version
from flask import Flask, render_template, request
import \
    mysql.connector  # imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import \
    Error, \
    connection  # import the Error class from mysql.connector module to handle exceptions that occur while interacting with the MySQL database
# this will handle database errors - when error occurs i.e. connection failure or syntax error the 'Error' exception will be raised
import logging  # import logging module to log errors if raised

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.ERROR)


def register_user(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return connection
    except mysql.connector.Error as error:
        print(f"The server could not connect to MySQL due to {error}")


@app.route("/")
def signup_form():
    return render_template("")  # insert html for signup form to call this function when user accesses the form


@app.route("/", methods=["POST"])  # after dash add in the route URL endpoint for the route
def signup():
    connection = get_db_connection()  # connection needs to be successful within the function
    if connection:
        try:
            name = request.form["name"]
            email = request.form["email"]
            username = request.form["username"]
            password = request.form["password"]
            # retrieve data from user input

            cursor = connection.cursor()
            query = "INSERT INTO users_table (name, email, username, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, username, password))
            connection.commit()  # insert data into mysql table
            cursor.close()
            logging.info("signup successful!")
        except mysql.connector.Error as error:
            logging.error(f"An error occurred: {error}")
        finally:
            connection.close()
    else:
        logging.error("An error has occurred")


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
        cursor = connection.cursor()
        # Insert SQL statements to create the tables
        create_users_table = """
            CREATE TABLE IF NOT EXISTS Users (
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
                FOREIGN KEY (user_id) REFERENCES Users (user_id)
            )
        """

        cursor.execute(create_users_table)
        cursor.execute(create_search_history_table)
        cursor.execute(create_locations_table)

        # maybe add logging.ingo here to confirm tables created successfully unless error raised

        logging.info("Tables created successfully")
    except Error as error:
        logging.error(f"The following error occurred when creating the tables {error}")
    finally:
        cursor.close()


# Main function
def main():
    # Establish database connection
    connection = get_db_connection()
    if connection:
        create_tables(connection)  # Create database tables
        connection.close()  # Close database connection
    else:
        logging.error("Error connecting to the database")


if __name__ == "__main__":
    main()


# insert data into database
def insert_location(connection, location_info):
    cursor = None #initialise cursor before the try/except block - set to None to avoid error
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
    finally:
        if cursor:
            cursor.close()  #check if the cursor is not none then close. prevents memory leaks
