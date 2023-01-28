#!/usr/bin/env python3
"""
HTTP server in python 3 for logging GET and POST requests
Hosting CSRF/DOM-XSS or other index.html deliver to victim as phishing/social engineering

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(content, 'utf8'))

    def do_GET(self):
        if self.path == '/':
            with open('index.html', 'r') as file:
                content = file.read()
            self._send_response(content)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode())
        self._send_response(post_data.decode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

run()
