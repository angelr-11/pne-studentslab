from Seq1 import Seq

s = Seq()
s.read_fasta("U5")
print(f"Sequence: (Length: {s.len()}) {s.str_bases[:50]} ...")
print("  Bases: ", s.count_())
print("  Rev:", s.reverse()[:50],"...")
print("  Comp:", s.complement()[:50],"...")