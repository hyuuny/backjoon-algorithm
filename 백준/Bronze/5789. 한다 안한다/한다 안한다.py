n = int(input())

for _ in range(n):
    s = input()
    mid = len(s) // 2

    print('Do-it') if s[mid - 1] == s[mid] else print('Do-it-Not')