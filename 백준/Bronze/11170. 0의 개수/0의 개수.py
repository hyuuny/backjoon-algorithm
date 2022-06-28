n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    cnt = 0
    for i in range(a, b + 1):
        # 숫자에 '0'이 포함된다면, 숫자의 '0' 개수를 cnt에 더한다.
        if '0' in str(i):
            cnt += str(i).count('0')

    print(cnt)