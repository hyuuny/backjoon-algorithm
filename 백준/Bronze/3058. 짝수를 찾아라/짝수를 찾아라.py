t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))

    odd_arr = [x for x in arr if x % 2 == 0]
    print(sum(odd_arr), min(odd_arr))