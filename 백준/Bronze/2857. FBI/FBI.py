import sys

flag = False
ans = []
for i in range(1, 5 + 1):
    name = sys.stdin.readline()

    if name.count('FBI') > 0:
        ans.append(str(i))
        flag = True

if not flag:
    print('HE GOT AWAY!')
else:
    print(" ".join(ans))
