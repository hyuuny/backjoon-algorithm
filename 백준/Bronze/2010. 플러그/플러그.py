import sys

n = int(sys.stdin.readline())

multi_tap = [int(sys.stdin.readline()) for _ in range(n)]
answer = sum(multi_tap) - (n - 1) if min(multi_tap) > 1 else 1
print(answer)