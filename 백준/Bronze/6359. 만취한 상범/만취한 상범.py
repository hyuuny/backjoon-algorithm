def dead_drunk():
    n = int(input())

    num = 2
    doors = [True] * (n + 1)
    for j in range(2, n + 1):
        for k in range(2, n + 1):
            if k % num == 0:
                if doors[k]:
                    doors[k] = False
                elif not doors[k]:
                    doors[k] = True
        num += 1
    return doors[1:].count(True)


for _ in range(int(input())):
    print(dead_drunk())
