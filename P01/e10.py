from Seq1 import Seq

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for i in genes:
    gene = Seq()
    gene.read_fasta(i)
    print(f"Gene {i}: Most frequent base: {gene.mfb_finder()}")

