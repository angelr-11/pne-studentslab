fibo1 = 0
fibo2 = 1
print(fibo1, fibo2, end=" ")
for i in range(1, 10):
    fiboentry = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fiboentry
    print(fiboentry, end= " ")