def process(s):
    arr = []
    start = 0
    while start <= len(s) - 1:
        arr.append(s[start:])
        start += 1

    for val in sorted(arr):
        print(val)


process(input())