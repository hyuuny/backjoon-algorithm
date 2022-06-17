smallers = []
for i in range(9):
    smallers.append(int(input()))

answer = []
for i in range(len(smallers)):
    for j in range(i + 1, len(smallers)):
        if smallers[i] + smallers[j] == sum(smallers) - 100:
            val_1 = smallers[i]
            val_2 = smallers[j]
            smallers.remove(val_1)
            smallers.remove(val_2)
            break

smallers.sort()
for small in smallers:
    print(small)
