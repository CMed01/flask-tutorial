import os
from flask import Flask, render_template


app = Flask(__name__)

"""
Code for routing websites to each other
"""
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

if __name__ == "__main__":
    """
        Only make debu = true when in development
        When launching will need to change this to false
        """
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)