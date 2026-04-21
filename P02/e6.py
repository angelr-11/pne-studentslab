from Seq1 import Seq
from client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
s = Seq()
seq = s.read_fasta("FRAT1")
c1.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases")
c2.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases")

print("Gene FRAT1:", seq[0:50],"...")

count = 1
for i in range(0, 100, 10):
    fragment = seq[i: i + 10]
    print(f"Fragment {count}: {fragment}")
    if count % 2 == 0:
        c2.talk(f"Fragment {count}: {fragment}")
        count += 1
    else:
        c1.talk(f"Fragment {count}: {fragment}")
        count += 1