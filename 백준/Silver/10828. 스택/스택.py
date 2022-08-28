import sys


def process(stack):
    command = sys.stdin.readline().rstrip()

    # size
    if command == 'size': print(len(stack))

    # empty
    if command == 'empty': print(1) if stack == [] else print(0)

    # top
    if command == 'top': print(-1) if stack == [] else print(stack[-1])

    # pop
    if command == 'pop': print(-1) if stack == [] else print(stack.pop())

    # push
    if 'push' in command: stack.append(command[5:])


ans = []
for _ in range(int(sys.stdin.readline().rstrip())):
    process(ans)
