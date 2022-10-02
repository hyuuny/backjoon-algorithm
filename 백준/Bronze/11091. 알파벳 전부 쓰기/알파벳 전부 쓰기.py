def init_alphabet():
    alphabet = {}
    for i in range(97, 123):
        alphabet[chr(i)] = alphabet.setdefault(chr(i), 0)
    return alphabet


def solve():
    s = input()

    alpha = init_alphabet()
    for i in s.lower():
        if 97 <= ord(i) <= 122:
            alpha[i] += 1

    ans = ''
    for k, v in alpha.items():
        if alpha[k] == 0:
            ans += k

    return ans


for _ in range(int(input())):
    ans = solve()
    print('missing', ans) if ans != '' else print('pangram')
