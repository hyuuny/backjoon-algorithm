def stop(first):
    return first == -1


def solve(arr):
    cnt = 0
    for i in arr[:-1]:
        for j in arr[:-1]:
            if i != j and i == j * 2:
                cnt += 1
    return cnt


while True:
    arr = list(map(int, input().split()))

    if stop(arr[0]):
        break

    print(solve(arr))
