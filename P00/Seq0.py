from pathlib import Path

def seq_ping():
    print("OK")

def base_printer(fasta_file):
    b = Path(fasta_file).read_text().split("\n",1)
    body = b[1]
    body = body.replace("\n", "")
    return body
