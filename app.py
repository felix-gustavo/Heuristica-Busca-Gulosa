from flask import Flask, render_template, url_for
from Main import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)