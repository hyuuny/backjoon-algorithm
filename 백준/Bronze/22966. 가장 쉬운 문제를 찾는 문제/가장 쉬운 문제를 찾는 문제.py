n = int(input())
prob = {}

for _ in range(n):
    k, v = map(str, input().split())
    prob[k] = int(v)

ans = sorted(prob.items(), key=lambda x: x[1])
print(ans[0][0])