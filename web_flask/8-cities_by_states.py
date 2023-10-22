#!/usr/bin/python3
"""
A script that starts a Flask web application and displays cities by states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy session after each request.
    """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays a web page with a list of states and their cities.
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
