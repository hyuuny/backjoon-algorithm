a = list(map(int, input().split()))
b = list(map(int, input().split()))

winner = 0
for i in range(10):
    if a[i] > b[i]:
        winner += 1
    elif a[i] < b[i]:
        winner -= 1

if winner > 0:
    print("A")
elif winner < 0:
    print("B")
else:
    print("D")