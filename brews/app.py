from flask import Flask, jsonify
from brews.routes.users import user
from brews.settings import Config
from brews.extensions import db


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(Config)
    app.register_blueprint(user)
    with app.app_context():
        db.init_app(app)
    return app
