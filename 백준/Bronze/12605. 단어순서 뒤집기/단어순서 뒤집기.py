def solve():
    for i in range(int(input())):
        word = list(map(str, input().split()))[::-1]

        print('Case #%s:' % (i + 1), end=' ')

        word_len = len(word)
        for j in range(word_len):
            if j != word_len - 1:
                print(word[j], end=' ')
            else:
                print(word[j])


solve()
