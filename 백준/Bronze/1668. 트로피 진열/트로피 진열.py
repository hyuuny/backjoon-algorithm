def view_cnt(data):
    height = data[0]
    cnt = 1

    for i in range(1, len(data)):
        if height < data[i]:
            cnt += 1
            height = data[i]
    return cnt


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(view_cnt(arr))
arr.reverse()
print(view_cnt(arr))