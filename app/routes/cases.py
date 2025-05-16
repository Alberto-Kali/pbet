from flask import Blueprint, render_template, session, redirect, request, jsonify, url_for
from app.models import factory, User, Inventory, Items
from app.config import simple, rare, superrare, epic, mythical, legendary, precious
import random

cases_bp = Blueprint('cases', __name__, template_folder='templates')


def generate_case_items(case_type):
    case = []
    if case_type == 1 or case_type == 2:
        for i in range(18):
            pick = random.randint(0, 9)
            itog1 = simple[pick]
            argum = random.randint(300, 700)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(3):
            pick = random.randint(0, 9)
            itog1 = rare[pick]
            argum = random.randint(800, 1200)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 9)
        itog1 = superrare[pick]
        argum = random.randint(900, 1800)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 3 or case_type == 4:
        for i in range(10):
            pick = random.randint(0, 9)
            itog1 = simple[pick]
            argum = random.randint(500, 1000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(8):
            pick = random.randint(0, 9)
            itog1 = rare[pick]
            argum = random.randint(800, 1200)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(5):
            pick = random.randint(0, 9)
            itog1 = superrare[pick]
            argum = random.randint(800, 1300)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 8)
        itog1 = epic[pick]
        argum = random.randint(1000, 3000)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 5:
        for i in range(7):
            pick = random.randint(0, 9)
            itog1 = simple[pick]
            argum = random.randint(600, 800)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(12):
            pick = random.randint(0, 9)
            itog1 = rare[pick]
            argum = random.randint(900, 1200)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(7):
            pick = random.randint(0, 9)
            itog1 = superrare[pick]
            argum = random.randint(1200, 2200)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 8)
        itog1 = epic[pick]
        argum = random.randint(1000, 3000)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 6:
        for i in range(7):
            pick = random.randint(0, 9)
            itog1 = rare[pick]
            argum = random.randint(600, 1000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(12):
            pick = random.randint(0, 9)
            itog1 = superrare[pick]
            argum = random.randint(900, 1500)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(7):
            pick = random.randint(0, 8)
            itog1 = epic[pick]
            argum = random.randint(1400, 2000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 7)
        itog1 = mythical[pick]
        argum = random.randint(1000, 3000)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 7:
        for i in range(7):
            pick = random.randint(0, 9)
            itog1 = superrare[pick]
            argum = random.randint(600, 1000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(12):
            pick = random.randint(0, 8)
            itog1 = epic[pick]
            argum = random.randint(800, 1500)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(7):
            pick = random.randint(0, 7)
            itog1 = mythical[pick]
            argum = random.randint(1000, 3000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 7)
        itog1 = legendary[pick]
        argum = random.randint(1800, 3000)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 8:
        for i in range(7):
            pick = random.randint(0, 8)
            itog1 = epic[pick]
            argum = random.randint(600, 900)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(12):
            pick = random.randint(0, 7)
            itog1 = mythical[pick]
            argum = random.randint(800, 1000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(7):
            pick = random.randint(0, 7)
            itog1 = legendary[pick]
            argum = random.randint(1000, 4000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        pick = random.randint(0, 7)
        itog1 = precious[pick]
        argum = random.randint(1000, 1300)
        cost = round((itog1[2] * argum / 100), 2)
        itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
        case.append(itog2)
    elif case_type == 9:
        for i in range(7):
            pick = random.randint(0, 7)
            itog1 = mythical[pick]
            argum = random.randint(700, 1050)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for x in range(12):
            pick = random.randint(0, 7)
            itog1 = legendary[pick]
            argum = random.randint(800, 1600)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
        for j in range(7):
            pick = random.randint(0, 7)
            itog1 = precious[pick]
            argum = random.randint(1000, 4000)
            cost = round((itog1[2] * argum / 100), 2)
            itog2 = [itog1[1], cost, itog1[3], argum, itog1[5], itog1[4]]
            case.append(itog2)
    return case


def open_case(case_type, user, db_session, cost):
    case = generate_case_items(case_type)
    case = sorted(case, key=lambda y: y[0])
    vibor = case[random.randint(0, 21)]
    case[0] = vibor
    item = Items(name=vibor[4], cost=vibor[1], rname=vibor[0], rarity=vibor[2], color=vibor[5], w=vibor[3])
    db_session.add(item)
    db_session.commit()
    newItem = db_session.query(Items).filter_by(name=vibor[4], cost=vibor[1], rarity=vibor[2], w=vibor[3]).one()
    addAtUser = Inventory(item_id=newItem.id, user_id=user.id)
    db_session.add(addAtUser)
    db_session.commit()
    db_session.query(User).filter(User.id == user.id).update({'balance': (user.balance - cost)})
    db_session.commit()
    return vibor, case

@cases_bp.route("/case<case_type>open", methods=["GET"])
def case_open(case_type):
    print(case_open)
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    if user is None:
        return redirect(url_for('auth.login_user'))

    cost_map = {
        1: 50,
        2: 50,
        3: 200,
        4: 200,
        5: 350,
        6: 500,
        7: 650,
        8: 800,
        9: 1000
    }
    cost = cost_map.get(case_type, 50)

    vibor, case = open_case(int(case_type), user, db_session, cost)

    # Store the selected item and case in session or other storage to pass to case view
    session['selected_item'] = {
        "name": vibor[0],
        "cost": vibor[1],
        "rarity": vibor[2],
        "weight": vibor[3],
        "rname": vibor[4],
        "color": vibor[5]
    }
    session['case_items'] = [
        {
            "name": item[0],
            "cost": item[1],
            "rarity": item[2],
            "weight": item[3],
            "rname": item[4],
            "color": item[5]
        } for item in case
    ]
    session['user_balance'] = user.balance
    session['cost'] = cost

    return render_template("case.html", i=vibor, user=user, case=case, cost=str(cost))



@cases_bp.route("/case<case_type>")
def case_view(case_type):
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)

    selected_item = session.pop('selected_item', None)
    case_items = session.pop('case_items', None)
    user_balance = session.pop('user_balance', None)
    cost = session.pop('cost', None)
    case_description = session.pop('description', None)

    return render_template("viewcase.html", user=user, n=case_type,
                           selected_item=selected_item,
                           case_items=case_items,
                           name = case_type,
                           user_balance=user_balance,
                           cost="",
                           description = "ЗАЛУПАЗАЛУПАЗАЛУПА")
