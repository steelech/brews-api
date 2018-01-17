from flask import Blueprint, jsonify
from brews.models.models import User
from brews.extensions import db

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('', methods=["GET"])
def users():
    db.drop_all()
    db.create_all()
    first_user = User(username='charli', email='steelech@umich.edu')
    second_user = User(username='admin', email='admin@admin.com')
    db.session.add(first_user)
    db.session.add(second_user)
    db.session.commit()
    return jsonify({
        'message': 'hi'
        })
