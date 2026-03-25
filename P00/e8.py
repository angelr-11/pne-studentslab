import Seq0
genes = ["U5","RNU6_269P","FXN","FRAT1","ADA"]
print("-----| Exercise 8 |------")
for gene in genes:
    seq = Seq0.base_printer(f"../S04/sequences/{gene}.txt")
    print(f"Most frequent base for gene {gene}: {Seq0.mfb_finder(seq)}")