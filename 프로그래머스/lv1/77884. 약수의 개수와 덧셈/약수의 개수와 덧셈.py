def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        measure = 0
        num = 1
        while num <= i:
            # 수를 나눠서 0으로 떨어지면 약수
            if i % num == 0: measure += 1
            num += 1

        if measure % 2 == 0:
            answer += i
        elif measure % 2 == 1:
            answer -= i

    return answer


# 테스트를 위한 코드입니다.
print(solution(13, 17))
print(solution(24, 27))
print(solution(1, 2))