# 7개의 숫자 입력
data = [int(input()) for _ in range(7)]

# 홀수인 자연수만 list로
odd_num = [x for x in data if x % 2 == 1]

# 출력
if len(odd_num) > 0:
    print(sum(odd_num))
    print(min(odd_num))
else:
    print(-1)
