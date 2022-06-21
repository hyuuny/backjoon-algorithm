N = int(input())
data = sorted(list(set(map(int, input().split()))))
for i in data:
    print(i, end=" ")