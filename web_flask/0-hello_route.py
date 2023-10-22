#!/usr/bin/python3
'''Starts a Flask web application.
'''
from flask import Flask

app = Flask(__name__)


# Define the route for the URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB! """
    return "Hello HBNB!"


if _name_ == "_main_":
    # Start the Flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
