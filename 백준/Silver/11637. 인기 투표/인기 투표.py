t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    max_val = max(arr)

    if arr.count(max_val) > 1:
        print("no winner")
        continue

    idx = arr.index(max_val) + 1
    print('majority winner', idx) if sum(arr) - max_val < max_val else print('minority winner', idx)
