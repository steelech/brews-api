import graphene
from brews.models.models import Breweries
import pdb

class Hello(graphene.ObjectType):
    message = graphene.String()

class BreweryType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    street_address = graphene.String()
    locality = graphene.String()
    region = graphene.String()
    postal_code = graphene.String()
    phone = graphene.String()
    website = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()
    distance = graphene.Float()
    is_closed = graphene.String()
    formatted_address = graphene.String()
    rating = graphene.Float()
    rating = graphene.Float()


class Query(graphene.ObjectType):
    hello = graphene.Field(Hello)
    breweries = graphene.List(BreweryType, location=graphene.String(), radius=graphene.Float())

    def resolve_hello(self, info, **args):
        my_hello = Hello(message='Hello, world')
        return my_hello

    def resolve_breweries(self, info, **args):
        these_breweries = Breweries.get_by_location(location=args['location'], radius=args['radius'])
        new_breweries = [BreweryType(**brewery.to_json()) for brewery in these_breweries]
        return new_breweries


schema = graphene.Schema(query=Query)
