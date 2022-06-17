n = int(input())
tree_days = list(map(int, input().split()))

# 나무가 자라는데 오래 걸리는 순서대로 정렬
tree_days.sort(reverse=True)

for i in range(len(tree_days)):
    # 4 + 1 + 1 = 5
    # 3 + 2 + 1 = 6
    # 3 + 2 + 1 = 6
    # 2 + 4 + 1 = 6
    tree_days[i] = tree_days[i] + (i+1) + 1

print(max(tree_days))