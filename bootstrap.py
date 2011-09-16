#!/usr/bin/env python

"""
Bootstrap and serve your application. If you're in a development environment,
envoke the script with:

    $ python bootstrap.py

In a production environment, your application can be run with the `gevent`
Python library:

    $ python bootstrap.py --gevent
"""

import os
import argparse
from app import create_app


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--gevent', action='store_true',
                        help="Run gevent's production server.")
    args = parser.parse_args()
    return args.gevent


def serve_app(gevent_environment):
    """
    Serve your application. If `dev_environment` is true, then the
    application will be served using gevent's WSGIServer.
    """
    app = create_app()
    if gevent_environment:
        from gevent.wsgi import WSGIServer
        # Get the $PORT variable on heroku's environment.
        port = int(os.environ.get('PORT', 5000))
        http_server = WSGIServer(('', port), app)
        http_server.serve_forever()
    else:
        app.run(debug=True)


def main():
    dev_environment = parse_arguments()
    serve_app(dev_environment)


if __name__ == '__main__':
    main()
