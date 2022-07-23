def olympiad(n):
    arr = [list(map(int, input().split())) for _ in range(n)]
    sorted_arr = sorted(arr, key=lambda x: -x[2])

    ans = [sorted_arr[0][0:2], sorted_arr[1][0:2]]

    for i in sorted_arr[2:]:
        if ans[0][0] != i[0] or ans[1][0] != i[0]:
            ans.append((i[0], i[1]))

        if len(ans) == 3:
            break

    for i in ans:
        print(i[0], i[1])


n = int(input())
olympiad(n)