n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    words1 = {}
    for word in a:
        words1.setdefault(word, 0)
        words1[word] += 1

    words2 = {}
    for word in b:
        words2.setdefault(word, 0)
        words2[word] += 1

    print(a + " & " + b + " are anagrams.") if words1.items() == words2.items() else print(
        a + " & " + b + " are NOT anagrams.")