def solve():
    arr = [list(map(int, input().split())) for _ in range(9)]
    max_val, row, column = 0, 0, 0

    for i in range(9):
        for j in range(9):
            if arr[i][j] >= max_val:
                max_val = arr[i][j]
                row, column = i + 1, j + 1

    print(max_val)
    print(row, column)


solve()
