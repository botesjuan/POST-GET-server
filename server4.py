#!/usr/bin/env python3
"""
This implementation uses the socketserver module in Python to create a TCP server that listens on port 80. 
The handle method of the RequestHandler class is called whenever a request is received. 
It first splits the received data into individual lines and then extracts the request type and path from the first line. 
The remaining lines are treated as headers and added to a dictionary. 
If the request type is POST, the body of the request is also read and logged.

The log messages are written to a file named requests.log using the logging module in Python. 
The log level is set to logging.INFO so that only messages with the info level are recorded.

"""

import http.server
import logging
import sys
import socketserver

logger = logging.getLogger(__name__)

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        logger.debug(f"GET request received for path: {self.path}")
        logger.debug("Headers:")
        for key, value in self.headers.items():
            logger.debug(f"{key}: {value}")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode()
        logger.debug(f"POST request received for path: {self.path}")
        logger.debug("Headers:")
        for key, value in self.headers.items():
            logger.debug(f"{key}: {value}")
        logger.debug(f"Body: {body}")

logging.basicConfig(filename="requests.log", level=logging.DEBUG, stream=sys.stdout)

with socketserver.TCPServer(("0.0.0.0", 8090), RequestHandler) as server:
    server.serve_forever()
