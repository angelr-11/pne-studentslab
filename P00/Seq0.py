from pathlib import Path

#e1

def seq_ping():
    print("OK")

#e2

def base_printer(fasta_file):
    b = Path(fasta_file).read_text().split("\n",1)
    body = b[1]
    body = body.replace("\n", "")
    return body

#e3

def seq_len(body):
    return len(body)

#e4

def seq_count_base(gene):
    bases_app = {["A", 0],["T", 0],["C", 0],["G",0]}
    for i in range(len(gene)):

