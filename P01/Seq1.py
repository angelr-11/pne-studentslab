from importlib.resources import read_text
from pathlib import Path
class Seq:
    def __init__(self, str_bases=None):
        if str_bases is None:
            self.str_bases = "NULL"
            print("NULL sequence created")
        elif not len(str_bases) == str_bases.count("A") + str_bases.count("T") + str_bases.count("G") + str_bases.count("C"):
            self.str_bases = "ERROR"
            print("Invalid sequence")
        else:
            self.str_bases = str_bases
            print("New sequence created")

    def len(self):
        if self.str_bases == "NULL" or self.str_bases == "ERROR":
            return 0
        else:
            return len(self.str_bases)

    def scb(self, base):
        base_count = 0
        if base == "NULL" or base == "ERROR":
            return base_count
        else:
            for i in self.str_bases:
                if i == base:
                    base_count += 1
            return base_count

    def count_(self):
        bases = ["A", "C", "T", "G"]
        d = {}
        for i in bases:
            d[i] = self.scb(i)
        return d

    def reverse(self):
        if self.str_bases == "NULL" or self.str_bases == "ERROR":
            return self.str_bases
        else:
            return self.str_bases[::-1]

    def complement(self):
        if self.str_bases == "NULL" or self.str_bases == "ERROR":
            return self.str_bases
        else:
            complement = ""
            for i in range(len(self.str_bases)):
                if self.str_bases[i] == "A":
                    complement += "T"
                elif self.str_bases[i] == "T":
                    complement += "A"
                elif self.str_bases[i] == "G":
                    complement += "C"
                elif self.str_bases[i] == "C":
                    complement += "G"
            return complement

    def read_fasta(self,filename):
        file = f"../S04/sequences/{filename}.txt"
        contents = Path(file).read_text()
        split_c = contents.split("\n", 1)
        body = split_c[1]
        self.str_bases = body
        return self.str_bases
