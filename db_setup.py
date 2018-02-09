from brews.app import create_app, db
from brews.models.models import Brewery
from brews.lib.breweries.breweries import get_breweries

app = create_app()
with app.app_context():
    # db.drop_all()
    db.create_all()
    breweries = get_breweries()
    for brewery in breweries: # for later, make this a bulk insert
        db.session.add(brewery)
    db.session.commit()
