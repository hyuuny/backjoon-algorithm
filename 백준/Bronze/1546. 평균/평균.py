N = int(input())
arr = list(map(int, input().split()))
sum = 0

for i in arr:
    sum += (i / max(arr)) * 100

print(sum / len(arr))
