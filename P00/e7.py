import Seq0
x = "../S04/sequences/U5.txt"
seq = Seq0.base_printer(x)
print(f"Gene U5:\nfragment:{seq[:20]} \ncomplement:{Seq0.seq_complement(seq[:20])}")
