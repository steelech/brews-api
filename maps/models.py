class Place(object):
    def __init__(self, response):
        self.name = response['name']
        self.address = response['formatted_address']
        self.place_id = response['place_id']
        self.rating = response['rating']
        self.id = response['id']
        self.lat = response['geometry']['location']['lat']
        self.lng = response['geometry']['location']['lng']

    def to_json(self):
        return {
            'name': self.name,
            'address': self.address,
            'place_id': self.place_id,
            'rating': self.rating,
            'id': self.id,
            'lat': self.lat,
            'lng': self.lng,
        }
