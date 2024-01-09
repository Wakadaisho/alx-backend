#!/usr/bin/env python3

"""
Simple flask app with Babel config
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime
import pytz
from babel.dates import format_datetime


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Get locale from request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return request.args.get('locale')

    if (g.user):
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return request.headers.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """ Get user from dict
    """
    if user_id in users:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """ Before request
    """
    user_id = request.args.get('login_as')
    g.user = None
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user


@babel.timezoneselector
def get_timezone():
    """ Get timezone from request
    """
    g.timezone = None
    try:
        if (request.args.get('timezone')):
            tz = pytz.timezone(request.args.get('timezone'))
            return tz

        if (g.user):
            tz = pytz.timezone(g.user.get('timezone'))
            if tz:
                return tz
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/')
def index():
    """ GET /
    Return:
      - Render index.html
    """
    return render_template(
        '7-index.html',
        user=g.user,
        time=format_datetime(
            None,
            tzinfo=get_timezone(),
            locale=get_locale()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
