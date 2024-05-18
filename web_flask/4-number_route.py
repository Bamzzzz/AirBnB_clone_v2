#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application"""
from flask import Flask, escape

=======
"""
start Flask application
"""

from flask import Flask
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index_page():
    """Display 'Hello HBNB!'
    """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Display 'HBNB'
    """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """Display 'C' followed by the value of the text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space)
    """
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
<<<<<<< HEAD
def verify_int(n):
    """
    display “n is a number” only if n is an integer
    """
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
