from flask import Flask, render_template, request
from main import businesses

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/explore", methods=["GET", "POST"])
def explore():
    if request.method == 'POST':
        # get info from form
        location = request.form['location']
        # pass it to the API
        # businesses = func(location)
    return render_template("explore.html", businesses=businesses)

if __name__ == "__main__":
    app.run()