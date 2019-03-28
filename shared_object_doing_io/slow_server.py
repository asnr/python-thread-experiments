import time
import BaseHTTPServer

PORT = 8000

SECONDS_TO_WAIT = 0.2

class SlowServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(SECONDS_TO_WAIT)
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Thanks for waiting!\n')
        return

def serve():
    address = ('', PORT)
    server = BaseHTTPServer.HTTPServer(address, SlowServer)
    server.serve_forever()

if __name__ == '__main__':
    serve()
