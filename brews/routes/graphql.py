from flask import Blueprint, jsonify, request
from brews.extensions import db
from brews.graphql import schema
import json

graphql = Blueprint('graphql', __name__, url_prefix='/graphql')

@graphql.route('', methods=["POST"])
def handle_query():
    data = json.loads(request.data)
    result = schema.execute(data["query"], variable_values=data.get('variables', None)).data
    return jsonify({
        'data': result
    })
