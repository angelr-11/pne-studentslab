import socket
import termcolor
from P01 import Seq1

gene_names = ["U5","ADA","FRAT1", "FXN", "RNU6_269P"]
PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

while True:
    print("Waiting for connection...")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        command = msg_raw.decode().strip()
        parts = command.split()
        print(f"Incoming command: {termcolor.colored(command,"green")}")
        #e1
        if command == "PING":
            rs = "OK!"
        elif len(parts) == 2:
            #e2
            if parts[0] == "GET" and parts[1].isdigit() and 0 <= int(parts[1]) <= 4:
                n = int(parts[1])
                seqs = {0: "AAA", 1:"TTT", 2:"GGG", 3:"CCC", 4:"ATC"}
                rs = seqs.get(n,"error")
            #e3
            elif parts[0] == "INFO":
                eseq = Seq1.Seq(parts[1])
                if eseq.str_bases == "ERROR" or eseq.str_bases == "NULL":
                    rs = "NON VALID SEQUENCE"
                else:
                    rs = f"""Sequence: {eseq.str_bases}
                    Total length: {eseq.len()}
                    A: {eseq.scb("A")} ({round((eseq.scb("A")/eseq.len())*100,2)}%)
                    C: {eseq.scb("C")} ({round((eseq.scb("C")/eseq.len())*100,2)}%)
                    G: {eseq.scb("G")} ({round((eseq.scb("G")/eseq.len())*100,2)}%)
                    T: {eseq.scb("T")} ({round((eseq.scb("T")/eseq.len())*100,2)}%)\n"""
                    print(rs)
            #e4
            elif parts[0] == "COMP":
                eseq = Seq1.Seq(parts[1])
                rs = f"""Sequence: {eseq.str_bases}\nComplement: {eseq.complement()}\n"""
                print(eseq.complement())
            #e5
            elif parts[0] == "REV":
                eseq = Seq1.Seq(parts[1])
                rs = f"""Sequence: {eseq.str_bases}\nReverse: {eseq.reverse()}\n"""
                print(eseq.reverse())
            #e6
            elif parts[0] == "GENE" and parts[1] in gene_names:
                gene = Seq1.Seq()
                rs = f"""Gene {parts[1]}: {gene.read_fasta(parts[1])}\n"""



        else:
            rs = "error"



        cs.send(f"{rs}".encode())
        cs.close()

