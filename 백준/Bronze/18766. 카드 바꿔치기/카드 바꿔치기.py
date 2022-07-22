def change_card():
    n = int(input())

    cards1 = list(map(str, input().split()))
    cards2 = list(map(str, input().split()))

    flag = False
    for card in cards2:
        if cards1.count(card) != cards2.count(card):
            flag = True
            break

    print("CHEATER") if flag else print("NOT CHEATER")


for _ in range(int(input())):
    change_card()
