def solve(n):
    arr = []
    for i in range(1, n + 1):
        replace_val = str(i).replace("4", "").replace("7", "")
        if replace_val == "":
            arr.append(i)

    if arr[-1] == n:
        print(n)
    else:
        print(arr[-1])


solve(int(input()))
