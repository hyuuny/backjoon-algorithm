def solution(s):
    arr = sorted(list(map(int, s.split())))
    return str(arr[0]) + ' ' + str(arr[-1])


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
