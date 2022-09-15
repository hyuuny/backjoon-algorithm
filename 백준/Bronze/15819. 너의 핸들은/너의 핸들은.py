def solve(n, l):
    return sorted([input() for _ in range(n)])[l - 1]


n, l = map(int, input().rstrip().split())
print(solve(n, l))