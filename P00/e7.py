import Seq0
from P00 import Seq0

gene = Seq0.base_printer("../S04/sequences/U5.txt")
print("-----| Exercise 7 |------")
print("Gene U5:")
print(f"fragment: {gene[:20]}\n"+f"complement:{Seq0.seq_complement(gene[:20])}")