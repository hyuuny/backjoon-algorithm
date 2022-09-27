def solve(m, n):
    num = 1
    arr = []
    while True:
        square_num = num ** 2
        if square_num > n:
            break

        arr.append(square_num)
        num += 1

    min_val = 0
    sum_val = 0
    for i in arr:
        if min_val == 0 and i >= m:
            min_val = i
        if m <= i <= n:
            sum_val += i

    if min_val == 0:
        print(-1)
    else:
        print(sum_val)
        print(min_val)


solve(int(input()), int(input()))
