def process(word):
    arr = []
    cnt = 0
    for i in word:
        if i == '(':
            arr.append(i)
        elif i == ')':
            if len(arr) == 0:
                cnt += 1
            else:
                arr.pop()
    return cnt + len(arr)


print(process(input()))