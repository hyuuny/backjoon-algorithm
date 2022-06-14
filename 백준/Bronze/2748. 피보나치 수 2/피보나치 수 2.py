n = int(input())

cache_list = [0 for _ in range(n + 1)]  # list[0]은 0이기 때문에, 0부터 n+1까지
cache_list[0] = 0
cache_list[1] = 1

for i in range(2, n + 1):
    # 메모이제이션!
    cache_list[i] = cache_list[i - 1] + cache_list[i - 2]

print(cache_list[n])