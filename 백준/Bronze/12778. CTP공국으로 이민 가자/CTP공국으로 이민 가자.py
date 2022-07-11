t = int(input())
alphabet = [chr(x) for x in range(65, 91)]

for _ in range(t):
    m, q = map(str, input().split())

    ans = []
    if q == 'C':
        arr = list(map(str, input().split()))
        for i in arr:
            ans.append(alphabet.index(i) + 1)
    else:
        arr = list(map(int, input().split()))
        for i in arr:
            ans.append(alphabet[i - 1])

    print(" ".join(map(str, ans)))