from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from database import Traveler
from database import Destination
from database import Volunteer
from database import Survey
from database import Offer

from maill import createMIMEText
from maill import send_email

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
    offers = Offer.select()
    return render_template("list.html", offers=offers)

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

@app.route("/create_volunteer", methods=["POST"])
def new_volunteer():
    interest = request.form["interest"]
    Volunteer.create(interest=interest )
    return redirect("/list")


@app.route("/create_survey", methods=["POST"])
def new_Survey():
    impression = request.form["impression"]
    why= request.form["why"]
    Survey.create(impression=impression, why=why )
    return redirect("/list")

@app.route("/create_offer", methods=["POST"])
def new_Offer():
    want = request.form["want"]
    where = request.form["where"]
    when = request.form["when"]
    gmaill = request.form["gmaill"]
    Offer.create(want=want,where=where,when=when,gmaill=gmaill )
    return redirect("/list")

@app.route("/lets_go/<id>", methods=["POST"])
def lets_go(id):
    offer = Offer.get(id=id)
    print("lets_go")
    # メールの送り主
    from_email = "vlontrip@gmail.com"
    # メール送信先
    to_email = "yubaseballfunya@gmail.com"
    # メール件名とメール本文
    subject = "【ボラントリップ】" + offer.want + " のやってみるボタンが押されました"
    message = f"""
どこ：{offer.where} 

いつ：{offer.when}
"""
    mime = createMIMEText(from_email, to_email, message, subject)
    send_email(mime)
    return redirect("/list")

app.run(host="0.0.0.0",debug=True)
