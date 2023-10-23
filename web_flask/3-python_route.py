#!/usr/bin/python3
"""Starts a Flask web application to display some messages
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Renders a simple message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Renders a simple message."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Renders "C" followed by the value of the text variable.
    Replaces any underscores in the variable with a space.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Renders 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
