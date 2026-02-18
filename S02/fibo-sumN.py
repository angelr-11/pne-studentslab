def fibonacci(n):
    fibo1 = 0
    fibo2 = 1
    fibolist = [0,1]
    for i in range(1, n):
        fibo_number = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo_number
        fibolist.append(fibo_number)
    return fibolist

def fibosum(n):
    total = 0
    for i in fibonacci(n):
        total += i
    return total

print("Sum of the first 5 terms of the fibonacci series:",fibosum(5))
print("Sum of the first 5 terms of the fibonacci series:",fibosum(10))