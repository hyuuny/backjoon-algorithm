A = int(input())
B = int(input())
C = int(input())

times = str(A * B * C)
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(times)):
    if times[i] != 0:
        result[int(times[i])] += 1

for i in result:
    print(i)