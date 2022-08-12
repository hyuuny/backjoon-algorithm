def tall_person(n):
    names = []
    heights = []
    for _ in range(n):
        name, height = map(str, input().split())
        names.append(name)
        heights.append(height)

    max_val = max(heights)
    ans = []
    for i in range(len(heights)):
        if heights[i] == max_val:
            ans.append(names[i])

    return " ".join(ans)


while True:
    n = int(input())
    if n == 0: break
    print(tall_person(n))
