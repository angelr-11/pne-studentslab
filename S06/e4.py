import termcolor

def print_seqs(seqs_list: list, color):
    for index, sequence in enumerate(seqs_list):
        termcolor.cprint(f"Sequence {index}: (length: {sequence.length}) {sequence.seq}", f"{color}")

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
            print("New sequence created")
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

termcolor.cprint("List 1:", "cyan")
print_seqs(seq_list1, "cyan")
print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
