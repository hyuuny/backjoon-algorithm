def ball(m):
    arr = [1, 2, 3]

    for _ in range(m):
        a, b = map(int, input().split())

        x = arr.index(a)
        y = arr.index(b)
        arr[x], arr[y] = arr[y], arr[x]

    return arr[0]


print(ball(int(input())))
