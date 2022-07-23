def weather_caster():
    arr = list(input())

    # 앞에 'c'가 있었는가..
    cloud = False
    # 구름 이동 거리
    move_cnt = 0
    # 결과 값
    ans = []
    for s in arr:
        # 'c'면 0 append 및 이동거리를 1로 초기화하자.
        if s == 'c':
            ans.append(0)
            move_cnt = 1
            cloud = True
        elif cloud and s == '.':
            # 앞에 'c'가 있었고, '.'이면 이동 거리 append 및 next 1 추가
            ans.append(move_cnt)
            move_cnt += 1
        else:
            # 'c'가 없었으니 -1 append
            ans.append(-1)

    # 결과값을 join해서 반환
    return " ".join(map(str, ans))


h, w = map(int, input().split())
for _ in range(h):
    print(weather_caster())
