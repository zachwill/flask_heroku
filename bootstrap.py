#!/usr/bin/env python

"""
Bootstrap and serve your application. If you're in a development environment,
envoke the script with:

    $ python bootstrap.py

You can also specify the port you want to use:

    $ python bootstrap.py 5555

You can easily test the production `tornado` server, too:

    $ python bootstrap.py --tornado

Alternatively, your application can be run with the `gevent` Python library:

    $ python bootstrap.py --gevent
"""

import argparse
from app import create_app


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('port', nargs='?', default=5000, type=int,
                        help="An integer for the port you want to use.")
    parser.add_argument('--gevent', action='store_true',
                        help="Run gevent's production server.")
    parser.add_argument('--tornado', action='store_true',
                        help="Run gevent's production server.")
    args = parser.parse_args()
    return args


def serve_app(environment):
    """
    Serve your application. If a server argument is not passed, then your
    application will be run through Flask's development server.
    """
    app = create_app()
    # Use the $PORT variable on heroku's environment.
    port = environment.port
    if environment.gevent:
        from gevent.wsgi import WSGIServer
        http_server = WSGIServer(('', port), app)
        http_server.serve_forever()
    elif environment.tornado:
        from tornado.wsgi import WSGIContainer
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(port)
        IOLoop.instance().start()
    else:
        app.run(debug=True, port=port)


def main():
    dev_environment = parse_arguments()
    serve_app(dev_environment)


if __name__ == '__main__':
    main()
