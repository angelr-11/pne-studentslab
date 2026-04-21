from Seq1 import Seq
from client0 import Client
import termcolor
PRACTICE = 2
EXERCISE = 4

genes = ["U5", "ADA", "FRAT1"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)
s = Seq()

for i in genes:
    m = f"Sending {i} Gene to the server"
    print("To server:", termcolor.colored(m,"blue"))
    print(f"From server:\n {c.talk(m)}")
    seq = s.read_fasta(i)[:50]
    print("To server:", termcolor.colored(seq,"blue"))
    print(f"From server:\n {c.talk(seq)}")
