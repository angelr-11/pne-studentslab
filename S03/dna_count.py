def counter(seq):
    total_len = 0
    a = 0
    t = 0
    g = 0
    c = 0
    for base in seq:
        total_len += 1
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        elif base == "T":
            t += 1
        elif base == " ":
            total_len -= 1
    return total_len,a,c,g,t

seq1 = input("Introduce the sequence:")
print("total_len:", counter(seq1)[0])
print("A:", counter(seq1)[1])
print("C:", counter(seq1)[2])
print("G:", counter(seq1)[3])
print("T:", counter(seq1)[4])

