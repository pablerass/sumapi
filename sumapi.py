# -*- coding: utf-8 -*-
"""Simple API with mathmatical functions for learning purposes."""
import sys
import tornado.ioloop
import tornado.web

LISTEN_PORT = 80

__version__ = '1.0'


# Handlers
class ApiHandler(tornado.web.RequestHandler):
    """Empty handler."""

    def get(self):
        """Generate an empty response."""
        pass


class SumHandler(tornado.web.RequestHandler):
    """Sum Handler."""

    def get(self):
        """Generate response with result of the sum."""
        self.write("1")


class VersionHandler(tornado.web.RequestHandler):
    """API version Handler."""

    def get(self):
        """Print API version."""
        self.write(__version__)


# Application
HANDLERS = [
    (r"/", ApiHandler),
    (r"/sum", SumHandler),
    (r"/version", VersionHandler),
]


def application():
    """Application."""
    return tornado.web.Application(HANDLERS)


def wsgi_application():
    """WSGI application."""
    return tornado.wsgi.WSGIApplication(HANDLERS)


def main(argv=None):
    """Main function."""
    app = application()
    app.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.current().start()


# Main
if (__name__ == "__main__"):
    sys.exit(main(sys.argv))
