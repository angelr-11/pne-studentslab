class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases
        print("New sequence created")

    def len(self):
        return len(self.str_bases)
