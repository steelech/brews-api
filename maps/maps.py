import requests
import pdb
import os
from .models import Place
PLACES_KEY = os.environ['PLACES_KEY']
GEOCODING_KEY = os.environ['GEOCODING_KEY']

BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

def build_query(location, radius=10000):
    return 'query=brewery,beer&location={}&radius={}&key={}'.format(location, radius, PLACES_KEY)

def get_places(location):
    response = requests.get('{}{}'.format(BASE_URL, build_query(location, 50000)))
    results = response.json()['results']
    places = [Place(result).to_json() for result in results]
    return places
