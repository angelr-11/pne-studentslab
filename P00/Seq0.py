def seq_ping():
    print("OK")

def base_printer(fasta_file):
    b = fasta_file.split("\n",1)
    body = b.replace(" ","")
    return body