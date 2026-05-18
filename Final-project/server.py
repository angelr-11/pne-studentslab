# All imports used
import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json
import jinja2 as j

# Constants used multiple times
PORT = 8080
PATH = "../Final-project/html/"
SERVER = "rest.ensembl.org"
PARAM = "?content-type=application/json"

# Important functions
# This takes the desired endpoint + parameter that the task requires and gives back the ensembl data as a dictionary
def connector(url):
    con = http.client.HTTPSConnection(SERVER)
    try:
        con.request("GET", url)
    except ConnectionRefusedError:
        print("Connection refused.")
        exit()
    r = con.getresponse()
    r1 = r.read().decode("utf-8")
    res = json.loads(r1)
    termcolor.cprint(f"Response received: {r.status} {r.reason}\n", "cyan")
    return res

# Teacher's function for jinja
def read_html_file(filename):
    contents = Path(PATH + filename).read_text()
    return j.Template(contents)

# helps simplify /info/assembly endpoint tasks
def get_assembly(species):
    return connector("/info/assembly/" + species + PARAM)

# This avoids having to define what the specific template is for operations
def render_html(filename, **params):
    template = read_html_file(filename)
    return template.render(**params)

# This is necessary in cases that a species name has spaces
# It needs to be translated to its scientific name first as that's how ensemble looks it up
def get_scientific_name(name):
    c = connector("/info/species" + PARAM)
    for s in c["species"]:
        if s["display_name"].lower().replace(" ", "_") == name.lower().replace(" ", "_"):
            return s["name"]
    return None
# Handler class
class TestHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format_:str, *args):
        pass

    def do_GET(self):
        termcolor.cprint(self.requestline+"\n", 'green')
        command = urlparse(self.path)
        print(command.path)
        user_input = parse_qs(command.query)
        if command.path == "/":
            contents = Path(PATH + "index.html").read_text()

        elif command.path == "/listSpecies":
            c = connector("/info/species" + PARAM)
            total = len(c["species"])
            if "limit" in user_input:
                l = int(user_input["limit"][0])
                species_list = c["species"][:l]
            else:
                l = "NONE"
                species_list = c["species"]
            names = [s["display_name"] for s in species_list]
            contents = render_html("listspecies.html", total=total, limit=l, species=names)

        elif command.path == "/karyotype" and "species" in user_input:
            sp = user_input["species"][0]
            sci = get_scientific_name(sp)
            if sci is None:
                contents = Path(PATH + "error.html").read_text()
            else:
                kar = get_assembly(sci).get("karyotype")
                if kar is None:
                    contents = Path(PATH + "error.html").read_text()
                else:
                    contents = render_html("karyotype.html", species=sp, karyotype=kar)

        elif command.path == "/chromosomeLength" and "species" in user_input and "chromo" in user_input:
            sp = user_input["species"][0]
            chromo = user_input["chromo"][0]
            sci = get_scientific_name(sp)
            if sci is None:
                contents = Path(PATH + "error.html").read_text()
            else:
                chromos = get_assembly(sci).get("top_level_region")
                if chromos is None:
                    contents = Path(PATH + "error.html").read_text()
                else:
                    d = None
                    for n in chromos:
                        if n["name"] == chromo:
                            d = n["length"]
                            break
                    if d is None:
                        contents = Path(PATH + "error.html").read_text()
                    else:
                        contents = render_html("chromosome.html", species=sp, chromosome=chromo, data=d)

        else:
            contents = Path(PATH + "error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()
        self.wfile.write(str.encode(contents))


socketserver.TCPServer.allow_reuse_address = True

#Server's main program
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()