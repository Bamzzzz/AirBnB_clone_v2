#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application for AirBnB clone"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page of States and their Cities
    """
    states = storage.all(State).values()
    cities = list()

    return render_template('8-cities_by_states.html',
                           states=states)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page of the States
    """
    states = storage.all(State)
    return render_template('7-states_list.html',
                           states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ display a HTML page with State, Cities and
    City objects linked to the State.
    """
    states = storage.all(State).values()

    for state in states:
        if id == state.id:
            return render_template('9-states.html',
                                   states=states, state=state)

    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db_conn(error):
    """Closes the database again at the end of the request.
    """
    storage.close()


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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 3c9f5b97ec01493e470a21385fae9bd3213f30f8
