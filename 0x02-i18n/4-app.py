#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


app: Flask = Flask(__name__)


class Config:
    """Babels configration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel: Babel = Babel(app)


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
        return render_template('4-index.html'), 200, {'Content-Language':
                                                      requested_locale}

    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
