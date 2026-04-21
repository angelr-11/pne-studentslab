from Seq1 import Seq
from client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)
s = Seq()
seq = s.read_fasta("FRAT1")
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases")

print("Gene FRAT1:", seq[0:50],"...")

count = 1
for i in range(0, 50, 10):
    fragment = seq[i: i + 10]
    print(f"Fragment {count}: {fragment}")
    c.talk(f"Fragment {count}: {fragment}")

