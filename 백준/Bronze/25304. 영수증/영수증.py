x = int(input())
product_cnt = int(input())

for _ in range(product_cnt):
    money, cnt = map(int, input().split())
    x -= money * cnt

print('Yes') if x == 0 else print('No')