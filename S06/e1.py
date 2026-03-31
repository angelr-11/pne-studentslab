class Seq:
    def __init__(self, seq: str):
        if self.seq_check(seq):
            self.seq = seq
            print("New sequence created")
        else:
            self.seq = "Error"
            print("ERROR")
    @staticmethod
    def seq_check(seq):
        return len(seq) == seq.count("A") + seq.count("T") + seq.count("G") + seq.count("C")

    def __str__(self):
        return f"{self.seq}"

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
