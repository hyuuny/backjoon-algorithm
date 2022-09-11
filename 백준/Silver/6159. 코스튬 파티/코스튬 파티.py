import sys


def costume_party(cows):
    count = 0
    for i in range(len(cows)):
        for j in range(i + 1, len(cows)):
            sum_size = cows[i] + cows[j]
            if sum_size <= s:
                count += 1

    return count


n, s = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
print(costume_party(arr))
