def print_seqs(seqs_list: list):
    for index, sequence in enumerate(seqs_list):
        print(f"Sequence {index}: (length: {sequence.length}) {sequence.seq}")

class Seq:
    def __init__(self, seq: str):
        if self.seq_check(seq):
            self.seq = seq
            self.length = len(seq)
        else:
            self.seq = "Error"
            print("ERROR")
    @staticmethod
    def seq_check(seq):
        return len(seq) == seq.count("A") + seq.count("T") + seq.count("G") + seq.count("C")

    def __str__(self):
        return f"{self.seq}"


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)