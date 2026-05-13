import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

for human in person["PEOPLE"]:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(human['Firstname'], human['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(human['age'])

    phoneNumbers = human['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    list_len = len(phoneNumbers)
    print(list_len)

    # Print all the numbers
    for j, i in enumerate(phoneNumbers):

        termcolor.cprint("  Phone " + str( j + 1) + ": ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(i.get("type"))
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(i.get("number"))
