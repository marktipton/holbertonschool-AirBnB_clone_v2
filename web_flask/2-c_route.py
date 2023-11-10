#!/usr/bin/python3
"""flask web app with a third route option"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
