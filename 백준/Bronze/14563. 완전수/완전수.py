def perfect_number(n):
    for i in n:
        arr = []
        for j in range(1, i + 1):
            if i % j == 0:
                arr.append(j)

        sum_val = sum(arr[:-1])
        if sum_val == arr[-1]:
            print("Perfect")
        elif sum_val < arr[-1]:
            print("Deficient")
        else:
            print("Abundant")


t = int(input())
perfect_number(list(map(int, input().split())))
