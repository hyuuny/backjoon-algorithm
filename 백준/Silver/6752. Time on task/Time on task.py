def time_on_task(t):
    c = int(input())
    minutes = sorted([int(input()) for _ in range(c)])
    ans = []
    for i in range(len(minutes)):
        if sum(ans) + minutes[i] <= t:
            ans.append(minutes[i])

    return len(ans)


print(time_on_task(int(input())))
