import requests
import os
from brews.models.models import Brewery
import pdb

BASE_URL = 'http://api.brewerydb.com/v2/locations'
SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
BREWERYDB_KEY = os.environ['BREWERYDB_KEY']
PLACES_KEY = os.environ['PLACES_KEY']

def nearby_search(brewery, radius):
    keyword = '{}, {}, {}, {} {}'.format(brewery.get('name', ''), brewery.get('streetAddress', ''), brewery.get('locality', ''), brewery.get('region', ''), brewery.get('postalCode', ''))
    query_txt = '?key={}&location={},{}&radius={}&query={}'.format(PLACES_KEY, brewery['latitude'], brewery['longitude'], radius, keyword)
    response = requests.get('{}{}'.format(SEARCH_URL, query_txt))
    return response.json()['results']


def get_page(page_num):
    response = requests.get('{}?key={}&region=Massachusetts&p={}'.format(BASE_URL, BREWERYDB_KEY, page_num)).json()
    return response

def get_breweries():
    response = get_page(1)
    total_results = response['totalResults']
    num_pages = response['numberOfPages']
    data = response['data']
    breweries = []

    for brewery in data:
        search_results = nearby_search(brewery, 2)
        if len(search_results):
            content = search_results[0]
            brewery['formatted_address'] = content['formatted_address']
            brewery['latitude'] = content['geometry']['location']['lat']
            brewery['longitude'] = content['geometry']['location']['lng']
            brewery['name'] = content['name']
            brewery['rating'] = content.get('rating', '')
        breweries.append(Brewery(**brewery))

    for page_num in range(2, num_pages + 1):
        response = get_page(page_num)
        data = response['data']
        for brewery in data:
            search_results = nearby_search(brewery, 2)
            if len(search_results):
                content = search_results[0]
                brewery['formatted_address'] = content['formatted_address']
                brewery['latitude'] = content['geometry']['location']['lat']
                brewery['longitude'] = content['geometry']['location']['lng']
                brewery['name'] = content['name']
                brewery['rating'] = content.get('rating')
            breweries.append(Brewery(**brewery))

    return breweries
