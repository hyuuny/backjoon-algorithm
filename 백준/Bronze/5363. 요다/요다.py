n = int(input())

for _ in range(n):
    s = list(map(str, input().split()))

    ans = s[2:]
    ans += s[0:2]

    print(" ".join(ans))