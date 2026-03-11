import Seq0

seqs = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 3 |------")
for i in range(len(seqs)):
    s = f"../S04/sequences/{seqs[i]}.txt"
    print(f"Length of gene {seqs[i]}:", Seq0.seq_len(Seq0.base_printer(s)))

