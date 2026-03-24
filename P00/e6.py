import Seq0
from P00.Seq0 import seq_reverse

gene = Seq0.base_printer("../S04/sequences/U5.txt")
print("------| Exercise 6 |------")
print("Gene U5")
print(f"fragment: {seq_reverse(gene,20)[0]}\n"+"reverse:",seq_reverse(gene,20)[1])
