from http.server import HTTPServer, BaseHTTPRequestHandler

class BaseHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = "<b><i>Hello from Effective Mobile!</i></b>"
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=BaseHTTPHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
