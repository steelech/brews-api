import graphene
from brews.lib.maps.maps import get_places
from brews.models.models import Breweries
import pdb

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

class BreweryType(graphene.ObjectType):
    name = graphene.String()
    street_address = graphene.String()
    locality = graphene.String()
    region = graphene.String()
    postal_code = graphene.String()
    phone = graphene.String()
    website = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()

class Query(graphene.ObjectType):
    places = graphene.List(Place, location=graphene.String(default_value='42.2808,-83.7430'))
    hello = graphene.Field(Hello)
    breweries = graphene.List(BreweryType, location=graphene.String(default_value='42.2808,-83.7430'), radius=graphene.Float(default_value=20.0))

    def resolve_places(self, info, **args):
        these_places = get_places(location=args['location'])
        new_places = [Place(**params) for params in these_places]
        return new_places

    def resolve_hello(self, info, **args):
        my_hello = Hello(message='Hello, world')
        return my_hello

    def resolve_breweries(self, info, **args):
        these_breweries = Breweries.get_by_location(location=args['location'], radius=args['radius'])
        new_breweries = [BreweryType(**brewery.to_json()) for brewery in these_breweries]
        return new_breweries


schema = graphene.Schema(query=Query)
