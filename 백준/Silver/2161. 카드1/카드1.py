def card_one(card):

    # 첫 번째 카드는 버리고 시작이니까 True
    next_throw = True
    while len(card) > 0:
        if next_throw:
            # 이번 카드는 버렸으니, 다음 카드는 버리지 않도록 False
            print(card.pop(0), end=" ")
            next_throw = False
        else:
            # 다음 카드를 버리도록 True로 변경 후, 맨 앞 카드를 뒤에 옮기고, 삭제
            next_throw = True
            card.append(card[0])
            card.pop(0)


n = int(input())
card = [i + 1 for i in range(n)]
card_one(card)