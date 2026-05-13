import json
import termcolor
from pathlib import Path


jsonstring = Path("people-e1.json").read_text()
person = json.loads(jsonstring)

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
