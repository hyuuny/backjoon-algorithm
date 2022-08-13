def line(N, L):
    cnt = 1
    arr = []
    while len(arr) < N:
        if str(cnt).count(str(L)) == 0:
            arr.append(cnt)
        cnt += 1

    return arr[-1]


n, l = map(int, input().split())
print(line(n, l))
