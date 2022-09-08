def equal_word_group_by():
    n = int(input())
    arr = [input() for _ in range(n)]
    ans = set("".join(sorted(i)) for i in arr)
    return len(ans)


print(equal_word_group_by())