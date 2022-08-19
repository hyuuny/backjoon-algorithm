def joi_and_ioi(s):
    arr = [0, 0]
    for i in range(len(s[:-2])):
        if s[i] + s[i + 1] + s[i + 2] == 'JOI':
            arr[0] += 1
        elif s[i] + s[i + 1] + s[i + 2] == 'IOI':
            arr[1] += 1

    return arr


ans = joi_and_ioi(input())
print(ans[0])
print(ans[1])