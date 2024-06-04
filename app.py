from flask import Flask, render_template, request, session, redirect, url_for, flash
import requests
from config import API_KEY
from database import get_db_connection
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

logging.basicConfig(filename='app.log', level=logging.ERROR)

class App:
# functions to configure the test for /tests/test_app.py 
    def __init__(self, test_config=None):
        self.app = app
        if test_config:
            self.app.config.update(test_config)
        self.setup_routes()

    def setup_routes(self):
        # Register routes only if they are not already registered
        if not self.app.view_functions.get('index'):
            self.app.add_url_rule("/", view_func=self.index, methods=["GET"])
        if not self.app.view_functions.get('explore'):
            self.app.add_url_rule("/explore", view_func=self.explore, methods=["GET", "POST"])
        if not self.app.view_functions.get('signin'):
            self.app.add_url_rule("/signin", view_func=self.signin, methods=["GET"])
        if not self.app.view_functions.get('submit_signin'):
            self.app.add_url_rule("/submit-signin", view_func=self.submit_signin, methods=["POST"])
        if not self.app.view_functions.get('submit_signup'):
            self.app.add_url_rule("/submit-signup", view_func=self.submit_signup, methods=["POST"])
        if not self.app.view_functions.get('signout'):
            self.app.add_url_rule("/signout", view_func=self.signout, methods=["GET", "POST"])
        if not self.app.view_functions.get('contact'):
            self.app.add_url_rule("/contact", view_func=self.contact, methods=["GET"])
        if not self.app.view_functions.get('submit_contact'):
            self.app.add_url_rule("/submit-contact", view_func=self.submit_contact, methods=["POST"])


    def index(self):
        return render_template("homepage.html")

#function handles two types of location requests which is sent to the yelp api and returned also handles displaying recent searches
    def explore(self):
        businesses = []
        current_location_used = 'false'
        user_id = session.get('user_id')
        if not user_id:
            session.clear()
            return redirect(url_for('signin'))
        if request.method == 'POST':
            if 'latitude' in request.form and 'longitude' in request.form:
                lat = request.form['latitude']
                lon = request.form['longitude']
                current_location_used = request.form.get('currentLocationUsed', 'false')
                businesses = self.get_businesses_by_coords(lat, lon)
            elif 'location' in request.form:
                location = request.form['location']
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO Search_History (user_id, searched_location) VALUES (%s, %s)",
                    (user_id, location)
                )
                connection.commit()
                cursor.close()
                connection.close()
                businesses = self.get_businesses(location)
        
        recent_searches = []
        connection = get_db_connection()
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
    
    def signin(self):
        return render_template("signin.html")

#function to find the matching user input from an existing account on the database if = true allows user access to explore page if not gives an error
    def submit_signin(self):
        username = request.form['username']
        password = request.form['password']
        connection = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users_table WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                session['username'] = user['username']
                session['user_id'] = user['user_id']
                return redirect(url_for('explore'))
            else:
                return 'Invalid credentials', 401
        except connection.Error as error:
            print(f"There was an error connecting to MySQL: {error}")
            return 'Database connection error', 500
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

#function to take user input to create an account in the database
    def submit_signup(self):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        connection = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Users_table (username, password, email) VALUES (%s, %s, %s)",
                (username, password, email)
            )
            connection.commit()
            
            cursor.execute("SELECT * FROM Users_table WHERE username = %s", (username,))
            user = cursor.fetchone()
            
            session['username'] = username
            session['user_id'] = user[0]
            
            return redirect(url_for('explore'))
        except connection.Error as error:
            print(f"There was an error connecting to MySQL: {error}")
            return 'Database connection error', 500
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def signout(self):
        session.clear()
        return redirect(url_for('index'))

#function for user inputted location requested to yelp api
    def get_businesses(self, location):
        url = f"https://api.yelp.com/v3/businesses/search?term=dog+friendly&open_now=true&sort_by=distance&location={location}"
        headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if 'businesses' in result:
            return result['businesses']
        else:
            print("Error: 'businesses' key not found in the response.")
            return []

#function for geolocation requesting to yelp api
    def get_businesses_by_coords(self, latitude, longitude):
        url = f"https://api.yelp.com/v3/businesses/search?term=dog+friendly&open_now=true&sort_by=distance&latitude={latitude}&longitude={longitude}"
        headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if 'businesses' in result:
            return result['businesses']
        else:
            print("Error: 'businesses' key not found in the response.")
            return []

    def contact(self):
        return render_template("contact.html")

#function takes user input from contact form and submits it into the database
    def submit_contact(self):
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        logging.debug(f"Received contact form submission: name={name}, email={email}, message={message}")

        try:
            logging.debug("Attempting to connect to the database")
            connection = get_db_connection()
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
        except connection as error:
            logging.error(f"There was an error connecting to MySQL: {error}")
            flash('There was an error submitting your message. Please try again later.', 'danger')
            return redirect(url_for('contact'))

if __name__ == "__main__":
    app_instance = App()
    app_instance.app.run(debug=True)
