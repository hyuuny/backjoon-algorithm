def solve():
    word = input()
    happy_cnt = word.count(':-)')
    sad_cnt = word.count(':-(')
    if happy_cnt == 0 and sad_cnt == 0:
        print('none')
    elif happy_cnt == sad_cnt:
        print('unsure')
    elif happy_cnt > sad_cnt:
        print('happy')
    else:
        print('sad')


solve()
