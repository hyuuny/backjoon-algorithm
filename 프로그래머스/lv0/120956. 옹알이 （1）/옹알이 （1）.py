def solution(babbling):
    answer = 0

    for i in babbling:
        replaced_babbling = i.replace('aya', ' ')
        replaced_babbling = replaced_babbling.replace('ye', ' ')
        replaced_babbling = replaced_babbling.replace('woo', ' ')
        replaced_babbling = replaced_babbling.replace('ma', ' ')

        replaced_babbling = replaced_babbling.replace(' ', '')
        if len(replaced_babbling) == 0:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
