n = int(input())
n_list = list(map(int, input().split()))
minimum = 0
n_list.sort()

for i in range(n):
  for j in range(i + 1):
    minimum += n_list[j]
print(minimum)