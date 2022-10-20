def solve():
    case = 1
    while True:
        word = input()
        check_word = input()

        if word == 'END' and check_word == 'END':
            break

        print('Case %d:' % case, 'same') if sorted(word) == sorted(check_word) else print('Case %d:' % case,
                                                                                          'different')
        case += 1


solve()