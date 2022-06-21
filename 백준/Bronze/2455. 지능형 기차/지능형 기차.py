answer = []
for i in range(4):
    out_cnt, in_cnt = map(int, input().split())

    if i == 0:
        answer.append(in_cnt)
    else:
        answer.append(answer[i - 1] - out_cnt + in_cnt)

print(max(answer))