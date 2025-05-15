from flask import Blueprint, render_template, session, redirect, request
from app.models import factory, User
from app.config import keyWords100

payments_bp = Blueprint('payments', __name__, template_folder='templates')

@payments_bp.route("/promo", methods=["GET", "POST"])
def promo():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    if request.method == "GET":
        return render_template("donate.html", user=user)
    code = request.form["code"]
    print(code)
    if code in keyWords100:
        db_session.query(User).filter(User.id == user_id).update({'balance': (user.balance + 10000)})
        db_session.commit()
    return redirect("/")