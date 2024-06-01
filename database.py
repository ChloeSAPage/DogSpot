#pip install mysql connector - latest version
import mysql.connector #imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import Error #import the Error class from mysql.connector module to handle exceptions that occur while interacting with the MySQL database
# this will handle database errors - when error occurs i.e. connection failure or syntax error the 'Error' exception will be raised
import logging #import logging module to log errors if raised

logging.basicConfig(filename='app.log', level=logging.ERROR)

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
        logging.error(f"There was an error connecting to MySQL: {error}") #log this error so not printed to the user
        return None

def create_tables(connection):
    try:
        cursor = connection.cursor()

        #Insert SQL statements to create the tables
        create_users_table = """
        CREATE TABLE IF NOT EXISTS Users (
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
            yelp_url VARCHAR(255)
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
        create_tables(connection) # Create database tables
        connection.close() # Close database connection
    else:
        logging.error("Error connecting to the database")

if __name__ == "__main__":
    main()