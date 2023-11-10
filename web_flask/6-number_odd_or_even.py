#!/usr/bin/python3
"""flask web app with a third route option"""
from flask import Flask, abort, render_template

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


@app.route('/number_template/<n>', strict_slashes=False)
def n_number_html(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def n_number_parity(n):
    if n.isdigit():
        if int(n) % 2 == 0:
            parity = 'even'
            return render_template(
                '6-number_odd_or_even.html',
                n=n,
                parity=parity
            )
        else:
            parity = 'odd'
            return render_template(
                '6-number_odd_or_even.html',
                n=n,
                parity=parity
            )
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
