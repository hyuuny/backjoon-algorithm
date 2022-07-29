def set_words(check_word):
    cnt = 0
    for i, str in enumerate(check_word):
        if str in s:
            cnt += 1

    return cnt


n, m = map(int, input().split())
s = [input() for _ in range(n)]
check_word = [input() for _ in range(m)]
print(set_words(check_word))