t = int(input())

for i in range(t):
    data = list(input().split())

    answer = float(data[0])
    for j in range(1, len(data)):

        if data[j] == '@':
            answer *= 3
        elif data[j] == '%':
            answer += 5
        else:
            answer -= 7

    print('%.2f' % answer)