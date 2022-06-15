n = int(input())

times = [300, 60, 10]
count = [0] * 3

for i in range(len(times)):
    count[i] += n // int(times[i])
    n %= times[i]

print('-1') if n > 0 else print(count[0], count[1], count[2])