#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from typing import Dict


app: Flask = Flask(__name__)


class Config:
    """Babels configration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel: Babel = Babel(app)


users: Dict[int, Dict] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> int:
    """Gets a user with a particular Id"""
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Set the user data as a global on flask.g.user."""
    user_id = request.args.get('login_as', type=int)

    g.user = get_user(user_id)


@babel.localeselector
def get_locale() -> str:
    """Gets best match language"""
    requested_locale = request.args.get('locale')

    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Return the index page"""
    requested_locale = request.args.get('locale')

    if requested_locale in app.config['LANGUAGES']:
        return render_template('5-index.html'), 200, {'Content-Language':
                                                      requested_locale}

    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
