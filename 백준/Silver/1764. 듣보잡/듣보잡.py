import sys


def no_listen_no_see(n, m):
    _dict = {}
    size = 0
    ans = []
    for _ in range(n + m):
        name = sys.stdin.readline().rstrip()
        # 초기화 되어 있지 않으면, 0으로 초기화
        _dict[name] = _dict.setdefault(name, 0)
        _dict[name] += 1

        # 1 이상이면, 듣도 보도 못 했다는 뜻
        if _dict[name] > 1:
            ans.append(name)
            size += 1

    print(size)
    for name in sorted(ans):
        print(name)


N, M = map(int, sys.stdin.readline().rstrip().split())
no_listen_no_see(N, M)