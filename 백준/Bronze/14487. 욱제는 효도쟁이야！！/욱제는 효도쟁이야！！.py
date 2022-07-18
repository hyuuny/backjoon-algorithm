n = int(input())
street = list(map(int, input().split()))
print(sum(street) - max(street))