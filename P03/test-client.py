from client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

test_seq = "AAAGGG"

for i in ["PING", "GET", "INFO", "COMP", "REV", "GENE"]:
    print(f"* Testing {i}...")
    if i == "GET":
        for j in range(4):
            print(c.talk(f"GET {j}\n"))
    elif i == "INFO" or i == "COMP" or i == "REV":
        print(c.talk(f"{i} {test_seq}\n"))
    elif i == "GENE":
        for k in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
            print(c.talk(f"GENE {k}\n"))
    else:
        print(c.talk(f"{i}\n"))

