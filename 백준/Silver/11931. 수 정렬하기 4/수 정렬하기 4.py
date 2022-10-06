import sys


def solve():
    return sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))], reverse=True)


[print(i) for i in solve()]
