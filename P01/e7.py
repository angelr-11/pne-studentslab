from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

sequences = [s1, s2, s3]

for i, s in enumerate(sequences, start=1):
    print(f"Sequence {i}: (Length: {s.len()}) {s.str_bases}")
    print("  Bases: ", s.count_())
    print("  Rev:", s.reverse())