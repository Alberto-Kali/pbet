from flask import Blueprint, render_template, request, redirect, session
from app.models import User, factory, Community
import random


community_bp = Blueprint('community', __name__, template_folder='templates')


@community_bp.route("/community", methods=["GET", "POST"])
def community():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    if request.method == "GET":
        return render_template("community.html", user=user)
    rname = str(request.form["rname"])
    name = str(request.form["name"])
    email = str(request.form["email"])
    cost = int(request.form["cost"])
    rarity = str(request.form["rarity"])
    history = str(request.form["history"])
    user_history = str(request.form["history_user"])
    img = request.files["file"]
    content = img.read()
    out = open(f"static/img/img{random.randint(0, 999999)}.png", "wb")
    out.write(content)
    out.close()
    newitem = Community(rname=rname, user_id=user_id, name=name, email=email, cost=cost, rarity=rarity, history=history, history_user=user_history)
    db_session.add(newitem)
    db_session.commit()
    return redirect("/")
