def solve():
    yt, yj = map(int, input().split())
    lose_num = 5

    while True:
        yj += yt
        if yj >= lose_num:
            return 'yt'

        yt += yj
        if yt >= lose_num:
            return 'yj'


print(solve())