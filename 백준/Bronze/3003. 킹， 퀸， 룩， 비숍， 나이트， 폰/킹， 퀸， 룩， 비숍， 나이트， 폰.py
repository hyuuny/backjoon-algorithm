arr = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
print(" ".join(list(map(str, [chess[i] - arr[i] for i in range(6)]))))