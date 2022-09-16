def solution(s):
    arr = []
    cnt = 0
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if i == ')' and len(arr) == 0:
                cnt += 1
            else:
                arr.pop()

    return cnt == 0 and len(arr) == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
