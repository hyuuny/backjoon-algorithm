n = int(input())
milk_street = list(map(int, input().split()))

answer = 0
for i in range(n):
    if answer % 3 == milk_street[i]:
        answer += 1

print(answer)