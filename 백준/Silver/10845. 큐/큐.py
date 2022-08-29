import sys
from collections import deque


def process(q):
    command = sys.stdin.readline().rstrip()

    # push
    if 'push' in command:
        q.append(command[5::])

    # pop
    if command == 'pop':
        print(-1) if len(q) == 0 else print(q.popleft())

    # size
    if command == 'size': print(len(q))

    # empty
    if command == 'empty': print(1) if len(q) == 0 else print(0)

    # front
    if command == 'front':
        print(-1) if len(q) == 0 else print(q[0])

    # back
    if command == 'back':
        print(-1) if len(q) == 0 else print(q[-1])


q = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    process(q)
