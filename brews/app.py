from flask import Flask, jsonify
from flask_cors import CORS
from brews.routes.users import user
from brews.routes.graphql import graphql
from brews.settings import Config
from brews.extensions import db
from brews.graphql import schema
from flask_graphql import GraphQLView


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(Config)
    app.register_blueprint(user)
    app.register_blueprint(graphql)
    CORS(app)
    with app.app_context():
        db.init_app(app)

    app.add_url_rule(
        '/graphiql',
        view_func=GraphQLView.as_view(
            'graphiql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )
    return app
