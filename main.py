import graphene
import json
from flask_graphql import GraphQLView
from flask import Flask, request, jsonify
import pdb
from maps.maps import get_places

app = Flask(__name__)

class Place(graphene.ObjectType):
    name = graphene.String()
    address = graphene.String()
    place_id = graphene.String()
    rating = graphene.Float()
    id = graphene.String()
    lat = graphene.Float()
    lng = graphene.Float()


class Query(graphene.ObjectType):
    place = graphene.Field(Place)
    places = graphene.List(Place)

    def resolve_place(self, info, **args):
        this_place = get_places('42.2706837,-83.74087019999999')[0]
        new_place = Place(**this_place)
        return new_place

    def resolve_places(self, info, **args):
        these_places = get_places('42.2706837,-83.74087019999999')
        new_places = [Place(**params) for params in these_places]
        return new_places

schema = graphene.Schema(query=Query)

app.add_url_rule(
    '/graphiql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.route('/graphql', methods=['POST'])
def hello():
    data = json.loads(request.data)
    result = schema.execute(data["query"]).data
    return jsonify(result)

if __name__ == '__main__':
    app.run()
