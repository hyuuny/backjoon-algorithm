n, k = map(int, input().split())
answer = []
for i in range(1, n + 1):
    if n % i == 0:
        answer.append(i)

print(answer[k - 1]) if len(answer) >= k else print(0)