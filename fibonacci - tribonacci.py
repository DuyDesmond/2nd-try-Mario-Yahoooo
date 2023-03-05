import math

n = int(input())

def fibonacci(x):

    fibo = []
    for i in range(x):
        fibo.append(0)

    fibo[0] = 0
    fibo[1] = 1 
    for i in range(2, x):
        fibo[i] = fibo[i-2] + fibo[i-1]

    return fibo 

print(fibonacci(n))

