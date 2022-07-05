import sys

n = int(sys.stdin.readline().rstrip())

cache_arr = [0] * (1000000 + 1)
cache_arr[1] = 1
cache_arr[2] = 2
for i in range(3, n + 1):
    cache_arr[i] = (cache_arr[i - 1] + cache_arr[i - 2]) % 15746

print(cache_arr[n])