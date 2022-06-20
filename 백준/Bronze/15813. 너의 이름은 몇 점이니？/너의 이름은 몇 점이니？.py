n = int(input())
word = input()
alpha = [chr(i) for i in range(65, 90 + 1)]

answer = 0
for j in word:
    answer += alpha.index(j) + 1

print(answer)