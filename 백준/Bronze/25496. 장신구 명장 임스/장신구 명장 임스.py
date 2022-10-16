def solve():
    p, n = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    cnt = 0
    for i in arr:
        if p < 200:
            cnt += 1
            p += i

    return cnt


print(solve())
