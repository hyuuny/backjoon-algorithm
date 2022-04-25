def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 1 else n

n = int(input())
print(fibonacci(n))