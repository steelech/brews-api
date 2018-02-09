from brews.extensions import db
from geopy.distance import vincenty
import pdb

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Brewery(db.Model):
    __tablename__ = "breweries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    street_address = db.Column(db.String(120), nullable=False)
    locality = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(120), nullable=False)
    postal_code = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    is_closed = db.Column(db.String(20))
    rating = db.Column(db.Float, nullable=False)
    formatted_address = db.Column(db.String(120))

    def __init__(self, **kwargs):
        self.name = kwargs['brewery']['name']
        self.street_address = kwargs.get('streetAddress', '')
        self.locality = kwargs.get('locality', '')
        self.region = kwargs.get('region', '')
        self.postal_code = kwargs.get('postalCode', '')
        self.phone = kwargs.get('phone', '')
        self.website = kwargs.get('website', '')
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)
        self.is_closed = kwargs.get('isClosed', None)
        self.rating = kwargs.get('rating', 0.0)
        self.formatted_address = kwargs.get('formatted_address', '')
        # self.google_places = kwargs.get('google_places', None)
        self.distance = None

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'street_address': self.street_address,
            'locality': self.locality,
            'region': self.region,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'website': self.website,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'is_closed': self.is_closed,
            'distance': self.distance,
            'formatted_address': self.formatted_address,
            'rating': self.rating
        }

    def get_distance(self, location_string, latitude, longitude):
        start = (latitude, longitude)
        end = (location_string.split(',')[0], location_string.split(',')[1])
        self.distance = vincenty(start, end).miles


class Breweries(object):
    @classmethod
    def get_all(self):
        return Brewery.query.all()

    @classmethod
    def get_by_location(self, location, radius=20):
        close_breweries = []
        all_breweries = Brewery.query.all()
        for brewery in all_breweries:
            brewery.get_distance(location, brewery.latitude, brewery.longitude)
            if brewery.distance < radius and brewery.is_closed == 'N':
                close_breweries.append(brewery)
        return close_breweries
