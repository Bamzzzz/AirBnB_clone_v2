#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application for AirBnB clone"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database again at the end of the request.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
