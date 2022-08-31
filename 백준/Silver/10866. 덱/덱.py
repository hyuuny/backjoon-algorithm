import sys
from collections import deque


def process():
    command = sys.stdin.readline().rstrip()

    # push_front
    if 'push_front' in command: dq.appendleft(command[11::])

    # push_back
    if 'push_back' in command: dq.append(command[10::])

    # pop_front
    if command == 'pop_front': print(dq.popleft()) if dq else print(-1)

    # pop_back
    if command == 'pop_back': print(dq.pop()) if dq else print(-1)

    # size
    if command == 'size': print(len(dq))

    # empty
    if command == 'empty': print(0) if dq else print(1)

    # front
    if command == 'front': print(dq[0]) if dq else print(-1)

    # back
    if command == 'back': print(dq[-1]) if dq else print(-1)


dq = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    process()