#!/usr/bin/env python

"""
Bootstrap and serve your application. If you're in a development environment,
envoke the script with:

    $ python bootstrap.py

You can also specify the port you want to use:

    $ python bootstrap.py 5555

In a production environment, your application can be run with the `gevent`
Python library:

    $ python bootstrap.py --gevent
"""

import argparse
from gevent.wsgi import WSGIServer
from app import create_app


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('port', nargs='?', default=5000, type=int,
                        help="An integer for the port you want to use.")
    parser.add_argument('--gevent', action='store_true',
                        help="Run gevent's production server.")
    args = parser.parse_args()
    return args


def serve_app(environment):
    """
    Serve your application. If `dev_environment` is true, then the
    application will be served using gevent's WSGIServer.
    """
    app = create_app()
    port = environment.port
    if environment.gevent:
        # Use the $PORT variable on heroku's environment.
        http_server = WSGIServer(('', port), app)
        http_server.serve_forever()
    else:
        app.run(debug=True, port=port)


def main():
    dev_environment = parse_arguments()
    serve_app(dev_environment)


if __name__ == '__main__':
    main()
