def start_game(num, ws, ls, ts, _dict):
    score = 0
    for i in range(num):
        name = input()

        # 해킹을 통해 알아낸 유저의 경우..
        if _dict.get(name):
            if _dict.get(name) == 'W':
                score += ws
            elif _dict.get(name) == 'L':
                if score - ls < 0:
                    score = 0
                else:
                    score -= ls
        # 해킹을 통해 알아내지 못한 유저는 무조건 패배한다.
        else:
            if score - ls < 0:
                score = 0
            else:
                score -= ls

        if score >= ts:
            return 'I AM NOT IRONMAN!!'

    return 'I AM IRONMAN!!'


n, p = map(int, input().split())
ws, ls, ts = map(int, input().split())

names = {}
for _ in range(p):
    k, v = map(str, input().split())
    names[k] = v

print(start_game(n, ws, ls, ts, names))