# -*- coding: utf-8 -*-
"""Simple API with mathmatical functions for learning purposes."""
import os
import sys
import tornado.ioloop
import tornado.web

LISTEN_PORT = 8888

__version__ = '1.0'


# Handlers
class ApiHandler(tornado.web.RequestHandler):
    """Empty handler."""

    def get(self):
        """Generate an empty response."""
        pass


class SumHandler(tornado.web.RequestHandler):
    """Sum Handler."""

    def get(self, op1, op2):
        """Generate response with result of the sum."""
        self.write(str(int(op1) + int(op2)))


class VersionHandler(tornado.web.RequestHandler):
    """API version Handler."""

    def get(self):
        """Print API version."""
        self.write(__version__)


# Application
HANDLERS = [
    (r"/", ApiHandler),
    (r"/(?P<op1>\d+)\+(?P<op2>\d+)", SumHandler),
    (r"/version", VersionHandler),
]


def application():
    """Application."""
    return tornado.web.Application(HANDLERS)


def main(argv=None):
    """Main function."""
    app = application()
    port = int(os.environ.get("PORT", LISTEN_PORT))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


# Main
if (__name__ == "__main__"):
    sys.exit(main(sys.argv))
