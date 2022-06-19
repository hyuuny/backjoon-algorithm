n = input()
s1 = n[:len(n) // 2]
s2 = n[len(n) // 2:]

sum1 = 0
for i in s1:
    sum1 += int(i)

sum2 = 0
for i in s2:
    sum2 += int(i)

print("LUCKY") if sum1 == sum2 else print("READY")
