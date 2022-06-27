amount = list(map(int, input().split()))
chicken_price = int(input()) * 2
total_amount = sum(amount)

print(total_amount - chicken_price) if total_amount >= chicken_price else print(total_amount)