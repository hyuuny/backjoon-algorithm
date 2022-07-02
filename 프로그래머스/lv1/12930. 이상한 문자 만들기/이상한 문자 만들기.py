def odd_or_even(answer, i, j):
    if j % 2 == 0:
        answer.append(i[j].upper())
    else:
        answer.append(i[j].lower())


def solution(s):
    words = s.split(" ")
    answer = []
    for i in words:
        for j in range(len(i)):
            odd_or_even(answer, i, j)
        answer.append(" ")

    answer.pop(-1)
    return "".join(answer)


# 테스트를 위한 코드입니다.
print(solution("try hello world"))
