def fibonacci(val):
    return val if val < 2 else fibonacci(val-1) + fibonacci(val-2)

print(fibonacci(int(input())))