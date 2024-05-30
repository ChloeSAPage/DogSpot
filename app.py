from flask import Flask, render_template, request
import requests
from config import API_KEY

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    if request.method == 'POST':
        location = request.form['location']
        businesses = get_businesses(location)
    else:
        businesses = []
    return render_template("explore.html", businesses=businesses)

@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

def get_businesses(location):
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term=Dogs+Friendly"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)  # Use requests.get instead of request.get
    result = response.json()
    return result["businesses"]

if __name__ == "__main__":
    app.run(debug=True)