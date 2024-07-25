from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def create():
    return render_template("create.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

app.run(host="0.0.0.0")