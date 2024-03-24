#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    function that return hello hbnb
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    function that return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    function that return c
    """
    return f'C {escape(text.replace("_", " "))}'


@app.route('/python/<text>', strict_slashes=False)
def c(text):
    """
    function that return python with input text
    """
    return f'Python {escape(text.replace("_", " "))}'


@app.route('/python', strict_slashes=False)
def c(text):
    """
    function that return Python is cool
    """
    return 'Python is cool'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
