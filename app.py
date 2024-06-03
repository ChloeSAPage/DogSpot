from flask import Flask, render_template, request, session, redirect, url_for, flash
import requests
from config import API_KEY
import mysql.connector #imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import Error
import logging

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Replace with a strong secret key

logging.basicConfig(filename='app.log', level=logging.ERROR)

class DatabaseInsertionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DatabaseConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)
@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    businesses = []
    current_location_used = 'false'  # Default value set to 'false'
    user_id = session.get('user_id')  # Get user_id from session, if it exists
    if not user_id:
        session.clear()
        return redirect(url_for('signin'))
    if request.method == 'POST':
        # Check if latitude and longitude are provided by the browser
        if 'latitude' in request.form and 'longitude' in request.form:
            lat = request.form['latitude']
            lon = request.form['longitude']
            current_location_used = request.form.get('currentLocationUsed', 'false')
            businesses = get_businesses_by_coords(lat, lon)
        elif 'location' in request.form:
            location = request.form['location']
            connection = mysql.connector.connect(
                host="localhost",
                user="newuser",
                password="new_password",
                database="pet_friendly_database"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Search_History (user_id, searched_location) VALUES (%s, %s)",
                (user_id, location)
            )
            connection.commit()
            cursor.close()
            connection.close()
            businesses = get_businesses(location)
    
    recent_searches = []
    connection = mysql.connector.connect(
        host="localhost",
        user="newuser",
        password="new_password",
        database="pet_friendly_database"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
    SELECT searched_location, MAX(search_date) as latest_search_date
    FROM Search_History
    WHERE user_id = %s
    GROUP BY searched_location
    ORDER BY latest_search_date DESC
    LIMIT 5
    """, (user_id,))

    recent_searches = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("explore.html", businesses=businesses, currentLocationUsed=current_location_used, recent_searches=recent_searches)

@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

@app.route("/submit-signin", methods=["POST"])
def submit_signin():
    username = request.form['username']
    password = request.form['password']
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="newuser",
            password="new_password",
            database="pet_friendly_database"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users_table WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = user['username']
            session['user_id'] = user['user_id']  # Set user_id in session
            return redirect(url_for('explore'))  # Redirect to the explore page
        else:
            return 'Invalid credentials', 401
    except mysql.connector.Error as error:
        print(f"There was an error connecting to MySQL: {error}")
        return 'Database connection error', 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

@app.route("/submit-signup", methods=["POST"])
def submit_signup():
    username = request.form['username']
    password = request.form['password']  # In a real app, hash this password before storing
    email = request.form['email']
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="newuser",
            password="new_password",
            database="pet_friendly_database"
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Users_table (username, password, email) VALUES (%s, %s, %s)",
            (username, password, email)
        )
        connection.commit()
        
        # Fetch the newly created user to get the user_id
        cursor.execute("SELECT * FROM Users_table WHERE username = %s", (username,))
        user = cursor.fetchone()
        
        session['username'] = username
        session['user_id'] = user[0]  # Assuming user_id is the first column in the Users table
        
        return redirect(url_for('explore'))  # Redirect to the explore page
    except mysql.connector.Error as error:
        print(f"There was an error connecting to MySQL: {error}")
        return 'Database connection error', 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
@app.route("/signout", methods=['GET', 'POST'])
def signout():
    # Clear all data from the session
    session.clear()
    return redirect(url_for('index'))


def get_businesses(location):
    url = f"https://api.yelp.com/v3/businesses/search?term=dog+friendly&open_now=true&sort_by=distance&location={location}"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    result = response.json()
    # Check if 'businesses' key exists in the result
    if 'businesses' in result:
        return result['businesses']
    else:
        # Handle the case where 'businesses' key is not present
        print("Error: 'businesses' key not found in the response.")
        return []


def get_businesses_by_coords(latitude, longitude):
    url = f"https://api.yelp.com/v3/businesses/search?term=dog+friendly&open_now=true&sort_by=distance&latitude={latitude}&longitude={longitude}"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    # Log the status code and the JSON response for debugging

    result = response.json()
    # Check if 'businesses' key exists in the result
    if 'businesses' in result:
        return result['businesses']
    else:
        # Handle the case where 'businesses' key is not present
        print("Error: 'businesses' key not found in the response.")
        return []
    
@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    logging.debug(f"Received contact form submission: name={name}, email={email}, message={message}")

    try:
        logging.debug("Attempting to connect to the database")
        connection = mysql.connector.connect(
            host="localhost",
            user="newuser",
            password="new_password",
            database="pet_friendly_database"
        )
        logging.debug("Successfully connected to the database")

        cursor = connection.cursor()
        query = "INSERT INTO contact_form (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()
        logging.debug("Inserted contact form submission into database")

        cursor.close()
        connection.close()

        flash('Thank you for contacting us!', 'success')
        return redirect(url_for('contact'))
    except Error as error:
        logging.error(f"There was an error connecting to MySQL: {error}")
        flash('There was an error submitting your message. Please try again later.', 'danger')
        return redirect(url_for('contact'))


if __name__ == "__main__":
    app.run(debug=True)