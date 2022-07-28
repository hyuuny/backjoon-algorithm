def process(t):
    case_val = 1
    for _ in range(t):
        n = int(input())
        arr = sorted(list(map(int, input().split())), reverse=True)

        ans = []
        while arr:
            money = arr.pop()
            if money * 100 // 75 in arr:
                ans.append(str(money))
                arr.remove(money * 100 // 75)

        print("Case #%d: %s" % (case_val, " ".join(ans)))
        case_val += 1


t = int(input())
process(t)
