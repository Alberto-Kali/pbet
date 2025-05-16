from flask import Blueprint, render_template, session, redirect
from app.models import factory, User, Inventory, Items
import random

index_bp = Blueprint('index', __name__, template_folder='templates')

@index_bp.route("/")
def index():
    cases = [
        {'id': 1, 'name': 'Обычный кейс', 'description': 'Шанс получить обычные NFT рыбы',
         'price': 50, 'icon': 'bi bi-box-seam', 'gradient_class': 'bg-blue-gradient'},
        {'id': 2, 'name': 'Обычный кейс', 'description': 'Шанс получить обычных NFT морских существ',
         'price': 50, 'icon': 'bi bi-star', 'gradient_class': 'bg-orange-gradient'},
        {'id': 3, 'name': 'Редкий кейс', 'description': 'Шанс получить редкие NFT рыбы',
         'price': 200, 'icon': 'bi bi-trophy', 'gradient_class': 'bg-purple-gradient'},
        {'id': 4, 'name': 'Редкий кейс', 'description': 'Шанс получить редкие NFT рыбы',
         'price': 200, 'icon': 'bi bi-type', 'gradient_class': 'bg-gold-gradient'},
        {'id': 5, 'name': 'Сверхредкий кейс', 'description': 'Неизвестный шанс сверхредкие уникальные NFT',
         'price': 350, 'icon': 'bi bi-lock', 'gradient_class': 'bg-blue-gradient'},
        {'id': 6, 'name': 'Эпический кейс', 'description': 'Шанс получить эпические NFT рыбы',
         'price': 500, 'icon': 'bi bi-collection', 'gradient_class': 'bg-orange-gradient'},
        {'id': 7, 'name': 'Мифический кейс', 'description': 'Шанс получить мифические NFT рыбы',
         'price': 650, 'icon': 'bi bi-compass', 'gradient_class': 'bg-purple-gradient'},
        {'id': 8, 'name': 'Легендарный кейс', 'description': 'Шанс получить легендарные NFT рыбы',
         'price': 800, 'icon': 'bi bi-tree', 'gradient_class': 'bg-silver-gradient'},
        {'id': 9, 'name': 'Драгоценный кейс', 'description': 'Шанс получить драгоценные NFT рыбы',
         'price': 1000, 'icon': 'bi bi-box-seam', 'gradient_class': 'bg-gold-gradient'}
    ]

    user_id = session.get("user_id")
    db_session = factory()
    user = db_session.get(User, user_id)
    return render_template("index.html", user=user, cases=cases)