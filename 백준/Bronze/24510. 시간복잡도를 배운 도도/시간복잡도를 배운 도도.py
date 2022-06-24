n = int(input())

cnts = []
for _ in range(n):
    s = input()
    for_cnt = s.count("for")
    while_cnt = s.count("while")
    cnts.append(for_cnt + while_cnt)

print(max(cnts)) if max(cnts) > 0 else print(0)