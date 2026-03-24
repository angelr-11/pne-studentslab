import Seq0

seqs = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 5 |------")

for seq in range(len(seqs)):
    desired_sequence = f"../S04/sequences/{seqs[seq]}.txt"
    clean_des_seq = Seq0.base_printer(desired_sequence)
    print(f"Gene {seqs[seq]}:",Seq0.seq_count_base(clean_des_seq))
