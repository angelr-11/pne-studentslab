import Seq0

gene = Seq0.base_printer("../S04/sequences/U5.txt")
print("------| Exercise 6 |------")
print("Gene U5:")
print(f"fragment: {Seq0.seq_reverse(gene,20)[0]}\n"+"reverse:",Seq0.seq_reverse(gene,20)[1])
