n = int(input())

for _ in range(n):
    t = int(input())

    arr = list(map(int, input().split()))
    print(min(arr), max(arr))