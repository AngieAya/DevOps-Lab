
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/health":
            data = {
                "status": "ok",
                "service": "devops-lab"
            }

        elif self.path == "/version":
            data = {
                "application": "devops-lab",
                "version": "1.0.0"
            }

        else:
            self.send_error(404)
            return

        body = json.dumps(data).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = HTTPServer(("127.0.0.1", 8000), Handler)

print("Servicio disponible en http://127.0.0.1:8000")
server.serve_forever()
