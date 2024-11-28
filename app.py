from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from database import Traveler
from database import Destination

app = Flask(__name__)

@app.route("/")
def create():
    return render_template("create.html")

@app.route("/search")
def search():
    destinations = []
    if request.args.get('search_word'):
        destinations = Destination.select().where(
            Destination.name.contains(request.args.get('search_word')))
        
    if request.args.get('category') == "自然":
        destinations = Destination.select().where(
            Destination.category == '自然')
        
    if request.args.get('category') == "アクティビティ":
        destinations = Destination.select().where(
            Destination.category == 'アクティビティ')
        
        
    if request.args.get('category') == "食べ物":
        destinations = Destination.select().where(
            Destination.category == '食べ物')
        
    if request.args.get('category') == "歴史":
        destinations = Destination.select().where(
            Destination.category == '歴史')
    return render_template("search.html", destinations=destinations)
    
@app.route("/map/<id>")
def map(id):
    destination = Destination.get(id=id)
    print(destination.name)
    return render_template("map.html", destination=destination)

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

@app.route("/matching")
def matching():
    return render_template("matching.html")


@app.route("/create", methods=["POST"])
def new_taveler():
    nickname = request.form["nickname"]
    age = request.form["age"]
    from_area = request.form["from_area"]
    allergy = request.form["allergy"]
    dislike = request.form["dislike"]
    interest = request.form["interest"]
    from_date = request.form["from_date"]
    to_date = request.form["to_date"]

    Traveler.create(name=nickname, age=age, from_area=from_area, allergy=allergy, dislike=dislike, interest=interest, from_date=from_date, to_date=to_date)
    return redirect("/search")


app.run(host="0.0.0.0",debug=True)
