#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
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
def python_text(text):
    """
    function that return python with input text
    """
    return f'Python {escape(text.replace("_", " "))}'


@app.route('/python', strict_slashes=False)
def python(text):
    """
    function that return Python is cool
    """
    return 'Python is cool'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    function that return is number
    """
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    function that return number to template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    function that return number to template
    """
    if n/2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
