def chicken_coupon_cnt(rank, students):
    ans = 0
    for i, score in enumerate(students):
        if rank == score[0]:
            ans += 1

    return ans


n = int(input())

students = []
for _ in range(n):
    students.append(list(map(int, input().split())))
students.sort(key=lambda x: (x[0], x[1]), reverse=True)

last_rank = students[4][0]
print(chicken_coupon_cnt(last_rank, students[5:]))