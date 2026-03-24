from pathlib import Path

#e1

def seq_ping():
    print("OK")

#e2

def base_printer(fasta_file):
    b = Path(fasta_file).read_text().split("\n", 1)
    body = b[1]
    body = body.replace("\n", "")
    return body

#e3

def seq_len(body):
    return len(body)

#e4

def seq_count_base(gene):
    bases_app = {"A": 0, "C": 0, "T": 0, "G": 0}
    for base in gene:
        if base in bases_app:
            bases_app[base] += 1
    return bases_app

def seq_reverse(seq, n):
    fragment = seq[:n]
    reverse = fragment[::-1]
    return fragment, reverse

def seq_complement(seq):
    complement = ""
    for i in range(len(seq)):
        if seq[i] == "A":
            complement += "T"
        elif seq[i] == "T":
            complement += "A"
        elif seq[i] == "G":
            complement += "C"
        elif seq[i] == "C":
            complement += "G"
    return complement
