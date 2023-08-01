#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel


app: Flask = Flask(__name__)


class Config:
    """Babels configration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """Return the index page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
