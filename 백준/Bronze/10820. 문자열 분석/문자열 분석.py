while True:
    try:
        ans = [0, 0, 0, 0]
        for i in input():
            if i == " ":
                ans[3] += 1
                continue

            if 'a' <= i <= 'z':
                ans[0] += 1
                continue

            if 'A' <= i <= 'Z':
                ans[1] += 1
                continue

            if 0 <= int(i) <= 9:
                ans[2] += 1

        print(" ".join(map(str, ans)))
    except EOFError:
        break
