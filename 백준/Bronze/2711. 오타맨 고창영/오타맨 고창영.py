t = int(input())

for _ in range(t):
    idx, word = map(str, input().split())

    answer = ""
    for i in range(len(word)):
        if i == int(idx)-1: continue
        answer += word[i]

    print(answer)