x, y = map(int, input().split())
cards = list(map(int, input().split()))

while y > 0:
    cards.sort()
    sum_val = sum(cards[0:2])
    cards[0] = sum_val
    cards[1] = sum_val
    y -= 1

print(sum(cards))
