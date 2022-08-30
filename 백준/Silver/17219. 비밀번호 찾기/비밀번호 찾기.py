import sys


def init_dit(n):
    _dic = {}
    for _ in range(n):
        address, pwd = sys.stdin.readline().rstrip().split()
        _dic[address] = _dic.setdefault(address, pwd)
    return _dic


def find_password(_dic, m):
    for _ in range(m):
        print(_dic[input()])


n, m = map(int, sys.stdin.readline().rstrip().split())
site = init_dit(n)
find_password(site, m)