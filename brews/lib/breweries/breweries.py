import requests
import os
from brews.models.models import Brewery
import pdb

BASE_URL = 'http://api.brewerydb.com/v2/locations'
BREWERYDB_KEY = os.environ['BREWERYDB_KEY']

def get_page(page_num):
    response = requests.get('{}?key={}&region=Michigan&p={}'.format(BASE_URL, BREWERYDB_KEY, page_num)).json()
    return response

def get_breweries():
    response = get_page(1)
    total_results = response['totalResults']
    num_pages = response['numberOfPages']
    data = response['data']
    breweries = []

    for brewery in data:
        breweries.append(Brewery(**brewery))

    for page_num in range(2, num_pages + 1):
        response = get_page(page_num)
        data = response['data']
        for brewery in data:
            breweries.append(Brewery(**brewery))

    return breweries
