def solve(m):
    keyboard = []
    for _ in range(m):
        a, b, c = map(str, input().rstrip().split())
        keyboard.append([int(a), int(b), c])

    for word in sorted(keyboard, key=lambda x: (x[1], x[0])):
        print(word[2], end="")


n, m = map(int, input().rstrip().split())
solve(m)
