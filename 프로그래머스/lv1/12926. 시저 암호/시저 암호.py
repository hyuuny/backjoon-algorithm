def solution(s, n):
    answer = ''

    up_dic = {}
    for i in range(65, 91):
        up_dic[i] = up_dic.setdefault(i, chr(i))

    low_dic = {}
    for i in range(97, 123):
        low_dic[i] = low_dic.setdefault(i, chr(i))

    for i in s:
        if i == ' ':
            answer += i
            continue

        if i.isupper():
            if ord(i) + n > 90:
                minus_val = ord(i) + n - 90
                answer += up_dic[64 + minus_val]
            else:
                answer += up_dic[ord(i) + n]
        elif i.islower():
            if ord(i) + n > 122:
                minus_val = ord(i) + n - 122
                answer += low_dic[96 + minus_val]
            else:
                answer += low_dic[ord(i) + n]

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z ", 4))
