def validate(s):
    return s.count('*') == 1


def init_alphabet():
    alphabet = {}
    for i in range(97, 123):
        alphabet[chr(i)] = alphabet.setdefault(chr(i), 0)
    return alphabet


def solve():
    dic_alpha = init_alphabet()
    for i in s:
        if dic_alpha[i] < 1:
            dic_alpha[i] = dic_alpha[i] + 1
    return dic_alpha.values()


while True:
    s = ''.join(list(map(str, input().rstrip().split())))
    if validate(s): break
    print("Y") if sum(solve()) == 26 else print("N")
