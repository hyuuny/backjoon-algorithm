import sys

def check(n, candy):
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1


def teacher(n, candy):
    tmps = [0 for _ in range(n)]
    for idx in range(n):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmps[(idx + 1) % n] = candy[idx]

    for idx in range(n):
        candy[idx] += tmps[idx]

    return candy


def candy_war():
    n, candy = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
    cnt = 0

    while not check(n, candy):
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)


for i in range(int(sys.stdin.readline())):
    candy_war()