def solve(n):
    binary_n = format(n, 'b')
    return int(binary_n[::-1], 2)


print(solve(int(input())))
