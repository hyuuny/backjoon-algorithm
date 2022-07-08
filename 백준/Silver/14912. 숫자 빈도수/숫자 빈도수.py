import sys

n, d = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(1, n + 1):
    # d가 포함될 때, i가 두 자릿수 이상이면  i를 문자로 변환하여 카운트를 구하고, 한자리면 카운트를 1증가 시키자
    if str(i).count(str(d)) > 0:
        if i > 9:
            cnt += list(str(i)).count(str(d))
        else:
            cnt += 1

print(cnt)