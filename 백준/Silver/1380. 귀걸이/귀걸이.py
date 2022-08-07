ans = []
cnt = 1
while True:
    n = int(input())

    if n == 0:
        break

    names = [input() for _ in range(n)]

    ring_names = {}
    for _ in range(2 * n - 1):
        a, b = list(map(str, input().split()))
        ring_names[a] = ring_names.get(a, 0) + 1

    for key, val in ring_names.items():
        if val == 1:
            print(cnt, names[int(key) - 1])
            cnt += 1
            continue
