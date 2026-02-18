def sumn(n):
    res = 0
    for i in range (1, n+1):
        res += i
    return res

print("Sum of the first 20 integers:", sumn(20))
print("Sum of the first 100 integers:", sumn(100))