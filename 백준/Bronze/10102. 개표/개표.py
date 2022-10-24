def solve():
    v = int(input())
    s = input()

    a_cnt = s.count('A')
    b_cnt = s.count('B')
    if a_cnt > b_cnt:
        return 'A'
    elif b_cnt > a_cnt:
        return 'B'
    else:
        return 'Tie'


print(solve())
