import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import termcolor
from pathlib import Path
import jinja2 as j


PORT = 8080
PATH = "./S16/html/"

def read_html_file(filename):
    contents = Path("../S16/html/" + filename).read_text()
    return j.Template(contents)

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        raw_path = self.path
        clean_path = urlparse(raw_path)
        usermsg = parse_qs(clean_path.query)
        command = self.requestline.split(" ")[1]

        if command in ["/", "/echo"]:
            contents = Path("../S16/html/form-1.html").read_text()
        elif "message" in usermsg:
            text = usermsg.get("message")[0]
            my_data = {"todisplay": text}
            template = read_html_file("echo.html")
            contents = template.render(context=my_data)

        else:
            contents = Path("../S16/html/error.html").read_text()




        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()
        self.wfile.write(str.encode(contents))

socketserver.TCPServer.allow_reuse_address = True

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
