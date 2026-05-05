import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import termcolor
from pathlib import Path
import jinja2 as j
from P01 import Seq1


PORT = 8080
PATH = "../P06/html/"
seqs = {"1":"AAATTT", "2":"TTTAAA", "3":"CCCGGG", "4":"GGGCCC", "5":"ATCGATCG"}
def read_html_file(filename):
    contents = Path(PATH + filename).read_text()
    return j.Template(contents)

class TestHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format:str, *args):
        pass

    def do_GET(self):
        termcolor.cprint(self.requestline+"\n", 'green')
        command = urlparse(self.path)
        print(command.path)
        usri = parse_qs(command.query)
        if command.path == "/":
            contents = Path(PATH + "index.html").read_text()
        elif command.path == "/ping":
            contents = Path(PATH + "ping.html").read_text()
        elif command.path == "/get" and "menu" in usri:
            n = usri.get("menu")[0]
            seq = seqs.get(n)
            template = read_html_file("get.html")
            contents = template.render(number=n, sequence=seq)
        elif command.path == "/gene" and "gene" in usri:
            gene = usri.get("gene")[0]
            seq = Seq1.Seq().read_fasta(gene)[:1000]
            template = read_html_file("gene.html")
            contents = template.render(gen=gene, sequence=seq)
        elif command.path == "/operation" and "opt" in usri and "an_seq" in usri:
            oper = usri.get("opt")[0]
            seq = usri.get("an_seq")[0]
            r = Seq1.Seq(seq)
            if oper == "Info":
                result_ = r.info()
            elif oper == "Comp":
                result_ = r.complement()
            elif oper == "Rev":
                result_ = r.reverse()
            template = read_html_file("operation.html")
            contents = template.render(sequence=seq, operation=oper, result = result_)
        else:
            contents = Path(PATH + "error.html").read_text()




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
        print("Server stopped by the user")
        httpd.server_close()
