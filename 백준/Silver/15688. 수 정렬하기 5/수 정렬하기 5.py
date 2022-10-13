import sys


def solve():
    return sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])


[print(i) for i in solve()]
