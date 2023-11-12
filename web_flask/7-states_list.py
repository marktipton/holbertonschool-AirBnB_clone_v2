#!/usr/bin/python3
"""flask web app connected to file and db storage"""
from flask import Flask, abort, render_template
from models import storage, storage.all()
from models import state

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template(
        'states_list.html',
        state_id=state.id,
        state_name=state.name
    )


@app.teardown_appcontext
def teardown_context():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
