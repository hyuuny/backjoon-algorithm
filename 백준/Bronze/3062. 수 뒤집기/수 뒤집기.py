t = int(input())

for _ in range(t):
    data = input()
    reversed_word = data[::-1]

    sum_val = str(int(data) + int(reversed_word))
    answer = True
    for i in range(len(str(sum_val))):
        if sum_val[0:] != sum_val[::-1]:
            answer = False

    print('YES') if answer else print('NO')