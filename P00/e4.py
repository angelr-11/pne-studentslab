import Seq0

seqs = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "T", "C", "G"]
print("-----| Exercise 4 |------")


for seq in seqs:
    desired_seq = Seq0.base_printer(f"../S04/sequences/{seq}.txt")
    print(seq)
    for base in bases:
        print(f"{base}: {Seq0.seq_count_base(desired_seq, base)}")