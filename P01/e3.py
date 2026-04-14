from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: {s1.str_bases}")
print(f"Sequence 2: {s2.str_bases}")
print(f"Sequence 3: {s3.str_bases}")
