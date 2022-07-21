import sys

sys.setrecursionlimit(10 ** 8)


def dfs(v):
    global cnt
    visited[v] = True

    for i in (v + stone[v], v - stone[v]):
        if 0 <= i < n and not visited[i]:
            cnt += 1
            dfs(i)


n = int(input())
stone = list(map(int, sys.stdin.readline().rstrip().split()))
s = int(input())
visited = [False] * (n + 1)
cnt = 1

dfs(s - 1)
print(cnt)