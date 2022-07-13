def take_away_chocolate(chocolate):
    day = 0
    cnt = 0
    min_chocolate_cnt = min(chocolate)
    for i in range(1, len(chocolate)):
        # 현재 초콜릿 개수가 이전 초콜릿 개수와 같거나 크고, 가장 작은 초코릿 개수보다 크다면..
        if chocolate[i - 1] <= chocolate[i] and min_chocolate_cnt < chocolate[i]:
            # 현재 초콜릿 개수가 이전 초콜릿 개수 작아질 때 까지 개수를 줄여주자.
            while chocolate[i] > chocolate[i - 1]:
                chocolate[i] -= 1
                cnt += 1
            day += 1

    print(cnt, day)


n, k = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
take_away_chocolate(sorted(arr))