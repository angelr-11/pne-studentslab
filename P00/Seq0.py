from pathlib import Path

#e1.txt

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

#e4 & e5

def seq_count_base(gene, base):
    base_count = 0
    for i in gene:
        if i == base:
            base_count += 1
    return base_count

#e6

def seq_reverse(seq, n):
    fragment = seq[:n]
    reverse = fragment[::-1]
    return fragment, reverse

#e7
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

#e8
def mfb_finder(seq):
    counter = {"A":0, "T":0, "C":0, "G":0}
    for i in seq:
        if i in counter:
            counter[i] += 1
    max_base = None
    max_count = -1
    for k in counter:
        if counter[k] > max_count:
            max_count = counter[k]
            max_base = k

    return max_base




