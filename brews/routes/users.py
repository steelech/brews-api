from flask import Blueprint, jsonify
from brews.models.models import User
from brews.extensions import db

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('', methods=["GET"])
def users():
    return jsonify({
        'message': 'hi'
        })
