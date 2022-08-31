import sys

# 입력
S = sys.stdin.readline().replace(' ', '')
match_words = 'UCPC'
idx = 0
for i in S:
    if i == match_words[idx]:
        idx += 1

    if idx == 4:
        print('I love UCPC')
        break

else:
    print('I hate UCPC')
