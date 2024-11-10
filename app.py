from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from database import Traveler

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

@app.route("/plan")
def plan():
    return render_template("plan.html")

@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/offer")
def offer():
    return render_template("offer.html")


@app.route("/create", methods=["POST"])
def new_taveler():
    nickname = request.form["nickname"]
    age = request.form["age"]
    Traveler.create(name=nickname, age=age)
    return redirect("/")


app.run(host="0.0.0.0",debug=True)
