import sys


def solve(n):
    names = {}
    for _ in range(n):
        name = sys.stdin.readline()
        names[name] = names.setdefault(name, 0) + 1

    for _ in range(n - 1):
        name = sys.stdin.readline()
        names[name] -= 1

    for k, v in names.items():
        if v == 1:
            print(k)
            return


solve(int(input()))
