def init():
    arr = []
    for _ in range(int(input())):
        name, d, m, y = map(str, input().rstrip().split())

        if len(m) == 1: m = '0' + m
        if len(d) == 1: d = '0' + d

        arr.append([name, y + m + d])

    return arr


def birth_day(arr):
    sorted_arr = sorted(arr, key=lambda x: x[1])
    print(sorted_arr[-1][0])
    print(sorted_arr[0][0])

def solve():
    arr = init()
    birth_day(arr)


solve()
