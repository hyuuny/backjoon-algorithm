def process(s):
    arr = []
    ans = 0
    for i in s:
        if i == '(':
            arr.append('(')
            ans += 1
        elif i == ')':
            # 괄호가 () )( () 이런식으로 맞지 않으면 NO
            if len(arr) == 0:
                return 'NO'
            ans -= 1
            arr.pop()

    return 'YES' if ans == 0 else 'NO'


for _ in range(int(input())):
    print(process(input()))
