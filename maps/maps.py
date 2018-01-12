import requests
import pdb
import os
PLACES_KEY = os.environ['PLACES_KEY']
GEOCODING_KEY = os.environ['GEOCODING_KEY']

BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
query = 'query=brewery,beer&location=42.2706837,-83.74087019999999&radius=10000&key=AIzaSyAmiae51cbjDuO0z31Eo8k3d_IAiZ6Q3XA'

def build_query(location, radius=10000):
    return 'query=brewery,beer&location={}&radius={}&key={}'.format(location, radius, PLACES_KEY)

response = requests.get('{}{}'.format(BASE_URL, build_query('42.2706837,-83.74087019999999', 10000)))
results = response.json()['results']
names = [result['name'] for result in results]
print(names)
