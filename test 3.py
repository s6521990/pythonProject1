def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
        print(sum)

n = 6
factorial(n)