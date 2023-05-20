from flask import Flask


def create_app():
    app = Flask(__name__)
    from src.CarSeller.routes.routes import main
    app.register_blueprint(main)
    return app

