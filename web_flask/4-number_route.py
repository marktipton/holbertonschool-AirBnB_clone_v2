#!/usr/bin/python3
"""flask web app with a third route option"""
from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text_w_spaces = text.replace('_', ' ')
    return f'C {text_w_spaces}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text_w_spaces = text.replace('_', ' ')
    return f'Python {text_w_spaces}'


@app.route('/number/<n>', strict_slashes=False)
def n_is_number(n):
    if n.isdigit():
        return f'{n} is a number'
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
