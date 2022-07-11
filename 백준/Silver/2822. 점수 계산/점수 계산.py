scores = {}
for i in range(1, 8 + 1):
    scores.setdefault(int(i), int(input()))

# 큰 점수부터 내림차순 정렬
sorted_scores = sorted(scores.values(), reverse=True)
# 더할 점수 5개를 별도의 변수에 저장
additional_val = sorted_scores[0:5]
print(sum(additional_val))

# additional_val에 포함된다면 index를 가져오자.
for key, value in scores.items():
    if value in additional_val:
        print(key, end=" ")