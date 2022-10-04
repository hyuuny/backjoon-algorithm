def solve(n):
    words = {}
    for _ in range(n):
        word = input()
        words[word.lower()] = words.setdefault(word.lower(), word)

    sorted_words = sorted(words.keys())
    return words[sorted_words[0]]


while True:
    n = int(input())
    if n == 0: break

    print(solve(n))
