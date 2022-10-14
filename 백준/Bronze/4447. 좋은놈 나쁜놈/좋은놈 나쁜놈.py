def solve():
    name = input()

    lower_name = name.lower()
    g_cnt = lower_name.count('g')
    b_cnt = lower_name.count('b')

    if g_cnt > b_cnt:
        print(name, 'is GOOD')
    elif b_cnt > g_cnt:
        print(name, 'is A BADDY')
    else:
        print(name, 'is NEUTRAL')


for _ in range(int(input())):
    solve()
