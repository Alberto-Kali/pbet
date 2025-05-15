from flask import Blueprint, jsonify, render_template, request, redirect, session
from app.models import factory, User, Inventory, Items
from sqlalchemy.exc import SQLAlchemyError

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route("/register", methods=["GET", "POST"])
def register_user():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    if user is not None:
        return "Чтобы добавить нового пользователя, разлогиньтесь из-под текущего."

    if request.method == "GET":
        return render_template("reg.html")

    name = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    password_again = request.form["confirm-password"]

    if password != password_again:
        return "Введённые пароли не совпадают."

    user = User(name=name, email=email)
    user.password = password

    try:
        db_session.add(user)
        db_session.commit()
    except SQLAlchemyError as e:
        db_session.rollback()
        return f"Не удалось добавить нового пользователя в базу: {e}"
    else:
        return redirect("/")


@auth_bp.route("/login", methods=['POST', 'GET'])
def login_user():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    if user is not None:
        return "Чтобы залогиниться под одним пользователем, разлогиньтесь из-под другого."

    next_url = request.args.get("next", "/")

    if request.method == "GET":
        return render_template(
            "sign.html",
            next_url=next_url
        )

    email = request.form["email"]
    password = request.form["password"]

    user = db_session.query(User).filter(User.email == email).first()

    if user is None:
        return "Пользователя с таким e-mail не существует."

    if password != user.password:
        return "Пароль пользователя введён неверно."

    session["user_id"] = user.id

    return redirect("/")


@auth_bp.route("/profile")
def profile():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    inventory = db_session.query(Inventory).filter(Inventory.user_id == user_id)
    inventorys = list()
    for i in inventory:
        a = db_session.query(Items).filter(Items.id == i.item_id)
        for x in a:
            b = [x.rname, x.cost, x.rarity, x.color, x.w]
            inventorys.append(b)
    return render_template("profile.html", user=user, inventory=inventorys)


@auth_bp.route("/collection", methods=['GET'])
def json_coll():
    db_session = factory()
    jobs = db_session.query(Items)
    result = []
    for x in jobs:
        result.append(
            x.to_dict()
        )
    return jsonify(result)


@auth_bp.route("/collectionpage")
def page_coll():
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    inventory = db_session.query(Items)
    inventorys = list()
    for i in inventory:
        b = [i.rname, i.cost, i.rarity, i.color, i.w]
        inventorys.append(b)
    return render_template("collection.html", user=user, inventory=inventorys)


@auth_bp.route("/logout")
def logout():
        session.pop("user_id", None)
        return redirect("/")
    