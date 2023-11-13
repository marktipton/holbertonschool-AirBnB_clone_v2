#!/usr/bin/python3
"""flask web app connected to file and db storage"""
from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display airbnb html page"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        cities=cities,
        amenities=amenities
    )


@app.teardown_appcontext
def teardown_context(exception):
    """remove current sqlalchemy session"""
    if hasattr(g, 'storage'):
        g.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
