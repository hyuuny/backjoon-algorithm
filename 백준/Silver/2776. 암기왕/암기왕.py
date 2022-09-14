import sys


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return 1

        # arr[mid]: 5, target: 3 -> arr[mid]: 4
        if arr[mid] > target:
            right = mid - 1

        # arr[mid]: 3, target: 5 -> arr[mid]: 4
        if arr[mid] < target:
            left = mid + 1

    return 0


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    note_one = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    m = int(sys.stdin.readline().rstrip())
    note_two = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in note_two:
        print(binary_search(note_one, i))
