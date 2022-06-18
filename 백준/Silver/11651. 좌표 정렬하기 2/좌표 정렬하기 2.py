n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
# y 좌표를 기준으로 오름차순 정렬
# y 좌표가 같다면 x 좌표를 기준으로 오름차순 정렬
sorted_datas = sorted(datas, key=lambda x: (x[1], x[0]))
for data in sorted_datas:
    print(data[0], data[1])