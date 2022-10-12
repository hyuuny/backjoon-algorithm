def solution(s):
    total_cnt = 0
    removed_zero_cnt = 0
    while s != '1':
        removed_zero_cnt += s.count('0')
        s_len = len(s.replace('0', ''))
        s = str(bin(s_len)[2:])
        total_cnt += 1

    answer = [total_cnt, removed_zero_cnt]
    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
