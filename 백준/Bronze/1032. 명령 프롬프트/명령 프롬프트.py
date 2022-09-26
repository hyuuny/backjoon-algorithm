def solve():
    n = int(input())

    ans = []
    for _ in range(n):
        word = input()

        if len(ans) == 0:
            for i in word:
                ans.append(i)

        for i in range(len(word)):
            if ans[i] == word[i]:
                continue
            else:
                ans[i] = '?'

    return "".join(ans)


print(solve())