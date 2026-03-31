def print_seqs(seqs_list: list):
    for index, sequence in enumerate(seqs_list):
        print(f"Sequence {index}: (length: {sequence.length}) {sequence.seq}")

def generate_seqs(pattern: str, n: int):
    generated = []
    next_char = ""
    for i in range(n):
        sequence = Seq(pattern).seq + next_char
        next_char = sequence
        generated.append(Seq(sequence))
    return generated

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


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
