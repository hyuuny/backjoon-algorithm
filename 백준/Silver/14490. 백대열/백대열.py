def maximum(n, m):

    # 최대한으로 약분할 수 있는 값
    max_val = 1
    # 1부터 n과 m 중 최소값 + 1만큼 반복하자.
    for i in range(1, min(n, m) + 1):
        # n과 m이 모두 나누어 진다면, 그 값을 저장하자.
        if n % i == 0 and m % i == 0:
            max_val = i

    print(n // max_val, end="")
    print(':', end="")
    print(m // max_val)


n, m = map(int, input().split(':'))
maximum(n, m)