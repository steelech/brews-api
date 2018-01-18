from brews.extensions import db
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

    def to_json(self):
        return {
            'name': self.name,
            'street_address': self.street_address,
            'locality': self.locality,
            'region': self.region,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'website': self.website,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
