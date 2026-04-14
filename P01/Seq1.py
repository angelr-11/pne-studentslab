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
        return len(self.str_bases)


