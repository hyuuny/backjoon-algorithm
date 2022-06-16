from sys import stdin


def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]


n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]
data.sort(reverse=True)

total_sum = 0
for i in range(n):
    if i % 3 != 2:
        total_sum += data[i]

print(total_sum)