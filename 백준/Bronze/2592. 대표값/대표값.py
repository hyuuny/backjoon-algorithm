import collections

datas = []
for _ in range(10):
    datas.append(int(input()))

_dict = {}
for i in datas:
    _dict.setdefault(i, 1)  # _dict에 해당 인덱스가 없으면 초기화, 있으면 무시
    _dict[i] += 1

print(int(sum(datas) / 10))
print(collections.Counter(_dict).most_common(n=1)[0][0])
