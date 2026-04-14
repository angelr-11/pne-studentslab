from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1.str_bases}")
print(f"Sequence 2: (Length: {s2.len()}) {s2.str_bases}")
print(f"Sequence 3: (Length: {s3.len()}) {s3.str_bases}")
