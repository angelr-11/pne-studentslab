from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

sequences = [s1, s2, s3]

for i, s in enumerate(sequences, start=1):
    print(f"Sequence {i}: (Length: {s.len()}) {s.str_bases}")
    print(f"A: {s.scb("A")}, C: {s.scb("C")}, T: {s.scb("T")}, G: {s.scb("G")}")