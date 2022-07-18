n = int(input())
levels = list(map(int, input().split()))
sorted_levels = sorted(levels, reverse=True)

max_level = max(sorted_levels[0:2])
max_gold = sum(sorted_levels[0:2])
for i in range(2, len(sorted_levels)):
    max_level = max(max_level, sorted_levels[i])
    max_gold += (max_level + sorted_levels[i])

print(max_gold)