import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

dq = deque([i for i in range(1, n + 1)])
while len(dq) != 1:
    # 제일 위의 카드를 버린다.
    dq.popleft()

    # 제일 위의 카드를 제일 아래로 옮긴다.
    dq.append(dq.popleft())

print(dq.pop())
