n = int(input())

for _ in range(n):
    s = input()
    print('skipped') if s.count('P') > 0 else print(eval(s))