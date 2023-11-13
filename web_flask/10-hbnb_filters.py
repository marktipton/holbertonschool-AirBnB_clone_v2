#!/usr/bin/python3
"""flask web app connected to file and db storage"""
from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """returns key value pair for states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_states_by_id(id):
    """returns key value pair for state when given id"""
    state = storage.get(State, id)
    return render_template('9-states.html', state=state, not_found=not state)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display airbnb html page"""
@app.teardown_appcontext
def teardown_context(exception):
    """remove current sqlalchemy session"""
    if hasattr(g, 'storage'):
        g.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
