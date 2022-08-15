def snow_white():
    arr = [int(input()) for _ in range(9)]
    calcul_val = sum(arr) - 100

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == calcul_val:
                x, y = arr[i], arr[j]
                arr.remove(x)
                arr.remove(y)
                return arr


[print(x) for x in snow_white()]
