import http.client
import termcolor
import json


SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print("Server:", SERVER)
print("URL:", URL)

conn = http.client.HTTPSConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("Connection refused.")

r1 = conn.getresponse()
termcolor.cprint(f"Response received: {r1.status} {r1.reason}\n", "cyan")

raw_data = r1.read().decode("utf-8")

response = json.loads(raw_data)

if response["ping"] == 1:
    print("WORKING!")

conn.close()