n, m = map(int, input().split())
stores = list(map(int, input().split()))

cnt = []
for i in range(max(stores)+1):
    cnt.append(stores.count(i))

print(max(cnt))