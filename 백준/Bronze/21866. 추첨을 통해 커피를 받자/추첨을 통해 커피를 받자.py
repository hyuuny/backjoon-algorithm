max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
n = list(map(int, input().split()))

hacker = False
score = 0
for i in range(9):
    if n[i] > max_scores[i]:
        hacker = True
        break
    score += n[i]

if hacker:
    print('hacker')
elif score >= 100:
    print('draw')
else:
    print('none')