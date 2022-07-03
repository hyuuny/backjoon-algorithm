def solution(s):
    mid = len(s) // 2
    if len(s) % 2 == 1:
        return s[mid]
    else:
        return s[mid-1] + s[mid]


# 테스트를 위한 코드입니다.
s = "abcde"
print(solution(s))

s = "qwer"
print(solution(s))