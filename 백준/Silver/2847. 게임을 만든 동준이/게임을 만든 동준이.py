n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
for idx in range(len(arr) - 1, 0, -1):
    if arr[idx] <= arr[idx - 1]:
        while arr[idx] <= arr[idx - 1]:
            arr[idx - 1] -= 1
            cnt += 1

print(cnt)