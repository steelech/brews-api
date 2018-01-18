import graphene
from brews.lib.maps.maps import get_places

class Place(graphene.ObjectType):
    name = graphene.String()
    address = graphene.String()
    place_id = graphene.String()
    rating = graphene.Float()
    id = graphene.String()
    lat = graphene.Float()
    lng = graphene.Float()
    location = graphene.String()

class Hello(graphene.ObjectType):
    message = graphene.String()

class Query(graphene.ObjectType):
    places = graphene.List(Place, location=graphene.String(default_value='42.2808,-83.7430'))
    hello = graphene.Field(Hello)

    def resolve_places(self, info, **args):
        these_places = get_places(location=args['location'])
        new_places = [Place(**params) for params in these_places]
        return new_places

    def resolve_hello(self, info, **args):
        my_hello = Hello(message='Hello, world')
        return my_hello

schema = graphene.Schema(query=Query)
