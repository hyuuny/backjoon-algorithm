N = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

answer = drinks[0]
for drink in drinks[1:]:
    answer += (drink/2)

# 절대/상대 오차는 10-5까지 허용
print(answer)