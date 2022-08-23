def parity(word):
    parity_cnt = word[0:-1].count('1')
    if parity_cnt % 2 == 0 and word[-1] == 'e':
        word = word.replace('e', '0')
    elif parity_cnt % 2 == 1 and word[-1] == 'e':
        word = word.replace('e', '1')
    elif parity_cnt % 2 == 0 and word[-1] == 'o':
        word = word.replace('o', '1')
    else:
        word = word.replace('o', '0')

    return word


while True:
    s = input()
    if s == '#': break
    print(parity(s))
