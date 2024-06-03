from flask import Flask, render_template, request, session, redirect, url_for
import requests
from config import API_KEY
import mysql.connector #imports mysql connector module which provides functions and classes to establish connection with mysql
from mysql.connector import Error

yelpAPI = YelpAPI(API_KEY)
app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Replace with a strong secret key

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
        # Handle the case where there is no user_id, perhaps by redirecting to the login page
        return redirect(url_for('signin'))
    if request.method == 'POST':
        # Check if latitude and longitude are provided by the browser
        if 'latitude' in request.form and 'longitude' in request.form:
            lat = request.form['latitude']
            lon = request.form['longitude']


            # Retrieve 'currentLocationUsed' from the form, default to 'false' if not present
            current_location_used = request.form.get('currentLocationUsed', 'false')
            businesses = get_businesses_by_coords(lat, lon)
        # Fallback to location if provided by the user
        elif 'location' in request.form:
            location = request.form['location']
                    # Store the search location in the database
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
        cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = user['username']
            session['user_id'] = user['user_id']  # Set user_id in session
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials', 401
    except Error as error:
        print(f"There was an error connecting to MySQL: {error}")
        return 'Database connection error', 500
    finally:
        if connection and connection.is_connected():
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
            "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)",
            (username, password, email)
        )
        connection.commit()
        session['username'] = username
        return redirect(url_for('index'))
    except Error as error:
        print(f"There was an error connecting to MySQL: {error}")
        return 'Database connection error', 500
    finally:
        if connection and connection.is_connected():
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

if __name__ == "__main__":
    app.run(debug=True)