arr = [list(map(int, input().split())) for _ in range(5)]

ans = [1, sum(arr[0])]
for i in range(1, len(arr)):
    if ans[1] < sum(arr[i]):
        ans = (i + 1, sum(arr[i]))

print(ans[0], ans[1])