def process(arr):
    cnt = 0
    while len(arr) > 0:
        # arr에서 가장 작은 값을 가져와서 반복하며 배수 만큼 지워주자!
        min_val = min(arr)
        for i in arr:
            if i % min_val == 0:
                arr.remove(i)
                cnt += 1

            # k번째라면, k번째 수를 반환하자!
            if cnt == k:
                return i


n, k = map(int, input().split())
print(process([x for x in range(2, n + 1)]))
