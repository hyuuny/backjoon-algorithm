n = int(input())
seat = list(map(int, input().split()))

init = []
answer = []
for i in seat:
    if i not in init:
        init.append(i)
    else:
        answer.append(i)

print(0) if len(answer) == 0 else print(len(answer))