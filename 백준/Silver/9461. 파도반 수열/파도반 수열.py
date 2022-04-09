dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

# 1, 1, 1, 2, 2, 3, 4, 5, 7
# 점화식 dp[n+3] = dp[n] + d[n+1]
# index[5]값 3은 index[2] + index[3]의 합이다.
for index in range(1, 98):
    dp[index+3] = dp[index] + dp[index + 1]

n = int(input())
for i in range(n):
    print(dp[int(input())])