from flask import Flask, render_template, request
from config import API_KEY
from yelpApi import YelpAPI

yelpAPI = YelpAPI(API_KEY)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    if request.method == 'POST':
        # Check if latitude and longitude are provided by the browser
        if 'latitude' in request.form and 'longitude' in request.form:
            lat = request.form['latitude']
            lon = request.form['longitude']
            businesses = yelpAPI.get_businesses_by_coords(lat, lon)
        # Fallback to location if provided by the user
        elif 'location' in request.form:
            location = request.form['location']
            businesses = yelpAPI.get_businesses(location)
        else:
            businesses = []
    else:
        businesses = []
    return render_template("explore.html", businesses=businesses)


@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

def get_businesses(location):
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term=Dogs+Friendly"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    
    # Log the status code and the JSON response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

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