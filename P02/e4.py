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
    m = termcolor.colored(f"Sending {i} Gene to the server", "blue")
    print("To server:", m)
    print(f"From server:\n {c.talk(m)}")
    seq = termcolor.colored(s.read_fasta(i)[:50], "blue")
    print("To server:", seq)
    print(f"From server:\n {c.talk(seq)}")
