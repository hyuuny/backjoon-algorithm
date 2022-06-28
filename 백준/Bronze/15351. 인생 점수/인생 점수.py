n = int(input())

for _ in range(n):
    s = input().replace(" ", "")
    words = {chr(65): 0, chr(66): 1}

    num = 1
    for i in range(65, 90 + 1):
        words[chr(i)] = num
        num += 1

    ans = 0
    for word in s:
        ans += words[word]

    print('PERFECT LIFE') if ans == 100 else print(ans)