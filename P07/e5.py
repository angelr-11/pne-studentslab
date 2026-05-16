import json
import http.client
from P01 import Seq1
import termcolor
from pathlib import Path

genes = json.loads(Path("../P07/genes.json").read_text())
g_names = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"
conn = http.client.HTTPSConnection(SERVER)

for gene in g_names:
    if gene in genes.keys():
        ENDPOINT = f"/sequence/id/{genes[gene]}"

        print("Server:", SERVER)
        print("URL:", SERVER + ENDPOINT + PARAMS)

        try:
            conn.request("GET", ENDPOINT + PARAMS)
        except ConnectionRefusedError:
            print("Connection refused.")
            exit()

        r1 = conn.getresponse()
        raw_data = r1.read().decode("utf-8")
        response = json.loads(raw_data)

        termcolor.cprint(f"Response received: {r1.status} {r1.reason}\n", "cyan")
        print(termcolor.colored("GENE:", "green"), gene)
        print(termcolor.colored("DESCRIPTION:", "green"), response["desc"])
        seq = Seq1.Seq(response["seq"])
        print(termcolor.colored("Total Length:", "green"), seq.len())
        d = seq.count_()
        for base, count in d.items():
            print(f"  {termcolor.colored(base,"blue")}: {count} ({round((count / seq.len()) * 100, 1)}%)")
        print(termcolor.colored("Most frequent base:", "green"), f"{seq.mfb_finder()}\n")

    else:
        print("Gene not found.")