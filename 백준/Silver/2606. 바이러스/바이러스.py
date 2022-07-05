import sys


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return True


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# 0번째 인덱스 사용 X
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

dfs(1)
# 1번 컴퓨터는 빼주자
print(visited.count(True) - 1)