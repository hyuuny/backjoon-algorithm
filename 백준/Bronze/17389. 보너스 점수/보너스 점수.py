n = int(input())
scores = input()

result = 0
bonus_score = 0
for i in range(len(scores)):
    if scores[i] == 'O':
        result += (i+1) + bonus_score
        bonus_score += 1
    else:
        bonus_score = 0

print(result)