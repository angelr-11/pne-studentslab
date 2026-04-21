import termcolor
from client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

for i in range(5):
    message = f"Test {i}"
    print("To server:", termcolor.colored(message,"blue"))
    print("From server:", termcolor.colored(c.talk(f"{message}\n"),"green"))
