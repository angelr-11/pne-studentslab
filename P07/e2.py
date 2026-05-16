import http.client
import termcolor
import json


g_names = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
genes = {}

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

conn = http.client.HTTPSConnection(SERVER)

print()
print("Dictionary of Genes!")
print(f"There are {len(g_names)} genes in the dictionary\n")


for gene in g_names:
    ENDPOINT = "/lookup/symbol/homo_sapiens/" + gene
    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("Connection refused.")

    r1 = conn.getresponse()
    raw_data = r1.read().decode("utf-8")
    response = json.loads(raw_data)

    g_id = response["id"]
    genes[gene] = g_id
    print(f"{termcolor.colored(gene, "green")}: --> {g_id}")

conn.close()