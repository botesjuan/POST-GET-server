#!/usr/bin/env python3
"""
This implementation uses the socketserver module in Python to create a TCP server that listens on port 8000. 
The handle method of the RequestHandler class is called whenever a request is received. 
It first splits the received data into individual lines and then extracts the request type and path from the first line. 
The remaining lines are treated as headers and added to a dictionary. 
If the request type is POST, the body of the request is also read and logged.

The log messages are written to a file named requests.log using the logging module in Python. 
The log level is set to logging.INFO so that only messages with the info level are recorded.

"""

import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(filename='logfile.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f'GET request received: {self.path}')
        print(f'GET request received: {self.path}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f'POST request received: {post_data}')
        print(f'POST request received: {post_data}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        logging.info(f'PUT request received: {put_data}')
        print(f'PUT request received: {put_data}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
