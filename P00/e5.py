import Seq0

seqs = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "T", "C", "G"]
print("-----| Exercise 5 |------")
dict_base_counts = {}

for seq in seqs:
    desired_seq = Seq0.base_printer(f"../S04/sequences/{seq}.txt")
    print(f"Gene {seq}")
    for base in bases:
        dict_base_counts.update({base:Seq0.seq_count_base(desired_seq, base)})
    print(dict_base_counts)
