N, L = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

for num in H:
    if num <= L:
        L += 1

# 출력
print(L)