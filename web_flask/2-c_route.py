#!/usr/bin/python3
"""Flask web application with multiple routes.

This module sets up a Flask web application with the following routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable.
  Replaces underscores with spaces.
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' on the main route.

    Returns:
        str: The string "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' on the /hbnb route.

    Returns:
        str: The string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by the value of the text variable.

    The function replaces underscores in the text variable with spaces.

    Args:
        text (str): The text to be displayed after "C ".

    Returns:
        str: The string "C " followed by the value of the text
             variable with underscores replaced by spaces.
    """
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
