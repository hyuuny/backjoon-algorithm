import sys


def number_game(m, n):
    global word_dict

    _dict = {}
    for i in range(m, n + 1):
        word = str(i)
        word_len = len(word)
        tem = ""
        for j in range(word_len):
            if j + 1 < word_len:
                tem += (word_dict[int(word[j])] + " ")
            else:
                tem += word_dict[int(word[j])]

        _dict[tem] = _dict.setdefault(tem, word)

    return _dict


m, n = map(int, sys.stdin.readline().rstrip().split())
word_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'there', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
             8: 'eight', 9: 'nine'}

ans = number_game(m, n)
print_cnt = 1
for i in sorted(ans.keys()):
    if print_cnt == 10:
        print(ans[i])
        print_cnt = 1
    else:
        print(ans[i], end=" ")
        print_cnt += 1
