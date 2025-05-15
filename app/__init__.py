from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.secret_key = "yandex_lyceum_secret_key"

    from app.routes.auth import auth_bp
    from app.routes.cases import cases_bp
    from app.routes.community import community_bp
    from app.routes.index import index_bp
    from app.routes.payments import payments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(cases_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(payments_bp)

    return app
