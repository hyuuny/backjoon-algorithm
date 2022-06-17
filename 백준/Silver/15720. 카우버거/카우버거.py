# 1. 값 입력받기
b, c, d = map(int, input().split())
min_len = max(b, c, d)
burgers = sorted(list(map(int, input().split())), reverse=True)
sides = sorted(list(map(int, input().split())), reverse=True)
beverages = sorted(list(map(int, input().split())), reverse=True)

# 2. 리스트를 순회하면서 각 값을 더하고, 최소 값에 더하기
min_len = min(b, c, d)
minimum_price = 0
for i in range(min_len):
    minimum_price += (burgers[i] + sides[i] + beverages[i]) * 0.9

# 3 최대값 출력
print(sum(burgers) + sum(sides) + sum(beverages))

# 4.1 각자 min_len 부터 끝까지 남은 값 모두 더하기
minimum_price += sum(burgers[min_len:])
minimum_price += sum(sides[min_len:])
minimum_price += sum(beverages[min_len:])

# 4.2 최소갑 출력
print(int(minimum_price))