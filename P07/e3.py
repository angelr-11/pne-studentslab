import http.client
import termcolor
import json
from pathlib import Path

genes = json.loads(Path("../P07/genes.json").read_text())
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/" + genes["MIR633"]
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

conn = http.client.HTTPSConnection(SERVER)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("Connection refused.")
    exit()

print()
print("Server:", SERVER)
print("URL:", URL)

r1 = conn.getresponse()
raw_data = r1.read().decode("utf-8")
response = json.loads(raw_data)

termcolor.cprint(f"Response received: {r1.status} {r1.reason}\n", "cyan")
print(termcolor.colored("GENE:", "green"), "MIR633")
print(termcolor.colored("DESCRIPTION:", "green"), response["desc"])
print(termcolor.colored("BASES:", "green"), response["seq"])

conn.close()