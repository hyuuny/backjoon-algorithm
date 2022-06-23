s = input().lower()
alphabet = [chr(x) for x in range(97, 122 + 1)]

ans = [0] * 26
for word in s:
    if word in alphabet:
        ans[alphabet.index(word)] += 1

for i in ans:
    print(i, end=" ")