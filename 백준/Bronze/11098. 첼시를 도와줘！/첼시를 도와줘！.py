def solve():
    p = int(input())

    max_price = 0
    ans = ""
    for _ in range(p):
        price, name = map(str, input().split())

        new_price = int(price)
        if new_price > max_price:
            max_price = new_price
            ans = name

    return ans


for _ in range(int(input())):
    print(solve())
