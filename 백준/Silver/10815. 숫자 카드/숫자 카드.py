import sys


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(sys.stdin.readline().rstrip())
cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
check_cards = list(map(int, sys.stdin.readline().rstrip().split()))

card_len = len(cards) - 1
ans = []
for card in check_cards:
    ans.append(binary_search(cards, card, 0, card_len))

print(" ".join(map(str, ans)))
