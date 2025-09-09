"""
A simple Flask application that returns "Hello World" on the root route.
"""

from flask import Flask

# Create a Flask WSGI application
app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Route for the root URL ('/').
    Returns:
        str: 'Hello World'
    """
    return "Hello World"


if __name__ == "__main__":
    # Run the Flask development server
    app.run()
