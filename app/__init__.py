"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flask import Flask
from views import views
import settings


def create_app():
    """Create your application."""
    app = Flask(__name__, static_folder='../static',
                template_folder='../templates')
    app.config.from_object(settings)
    app.register_blueprint(views)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
