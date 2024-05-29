from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # get info from form
    # display info
    return render_template("index.html")

if __name__ == "__main__":
    app.run()