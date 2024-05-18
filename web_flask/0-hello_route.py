#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application"""
from flask import Flask

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
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run('0.0.0.0')
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
