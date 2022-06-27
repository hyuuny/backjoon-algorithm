n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)

ans = 0
for i in range(n):
    tip = tips[i] - ((i + 1) - 1)
    ans += 0 if tip < 0 else tip

print(ans)