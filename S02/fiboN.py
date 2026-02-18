def fibonacci(n):
    fibo1 = 0
    fibo2 = 1
    for i in range(1, n):
        fibo_number = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo_number
    print(n,"th Fibonacci term:", fibo_number)

fibonacci(5)
fibonacci(10)
fibonacci(15)