N, L, K = map(int, input().split())

sub1, sub2 = 0, 0

for i in range(N):
    easy, hard = map(int, input().split())

    if hard <= L:
        sub2 += 1
    elif easy <= L:
        sub1 += 1

answer = min(sub2, K) * 140

if sub2 < K:
    answer += min(K - sub2, sub1) * 100

print(answer)