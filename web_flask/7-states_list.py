#!/usr/bin/python3
"""flask web app connected to file and db storage"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """returns key value pair for states"""
    states = storage.all(State).values()
    return render_template('states_list.html', states=states)



@app.teardown_appcontext
def teardown_context():
    """tear down """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
