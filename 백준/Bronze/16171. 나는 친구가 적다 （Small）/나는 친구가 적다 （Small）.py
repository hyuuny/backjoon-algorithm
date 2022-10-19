def solve():
    s = input()
    k = input()

    temp = ""
    for i in s:
        if i.isalpha():
            temp += i

    return 1 if temp.count(k) > 0 else 0


print(solve())
