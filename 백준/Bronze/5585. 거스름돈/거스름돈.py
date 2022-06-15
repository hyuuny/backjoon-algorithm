n = int(input())

coin_types = [500, 100, 50, 10, 5, 1] # 동전 타입
payback = 1000 - n # 거스름 돈
coin_count = 0 # 코인 갯수

for coin in coin_types:
    coin_count += payback // coin
    payback %= coin

print(coin_count)
