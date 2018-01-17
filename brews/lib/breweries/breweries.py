import requests
import os
from brews.models.models import Brewery

BASE_URL = 'http://api.brewerydb.com/v2/locations'
BREWERYDB_KEY = os.environ['BREWERYDB_KEY']

def get_breweries():
    response = requests.get('{}?key={}&region=Michigan'.format(BASE_URL, BREWERYDB_KEY)).json()
    data = response['data']
    numPages = response['numberOfPages']
    breweries = []
    for brewery in data:
        breweries.append(Brewery(**brewery))
    return breweries
