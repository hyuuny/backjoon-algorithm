while True:
    s = int(input())

    if s == 0: break

    while s > 9:
        s = sum(map(int, list(str(s))))

    print(s)