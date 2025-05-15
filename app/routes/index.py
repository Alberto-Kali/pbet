from flask import Blueprint, render_template, session, redirect
from app.models import factory, User, Inventory, Items
import random

index_bp = Blueprint('index', __name__, template_folder='templates')

@index_bp.route("/")
def index():
    cases = [
        {'id': 1, 'name': 'Обычный кейс', 'description': 'Шанс получить обычные NFT рыбы', 
         'price': 50, 'icon': 'bi bi-box-seam', 'gradient_class': 'bg-blue-gradient'},
        {'id': 2, 'name': 'Обычный кейс', 'description': 'Шанс получить обычные NFT рыбы', 
         'price': 50, 'icon': 'bi bi-box-seam', 'gradient_class': 'bg-blue-gradient'},
        # ... остальные кейсы
    ]
    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    return render_template("index.html", user=user, cases=cases)