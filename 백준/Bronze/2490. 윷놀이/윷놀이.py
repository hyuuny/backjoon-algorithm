_list = [list(map(int, input().split())) for _ in range(3)]
answers = [i.count(0) for i in _list]

for i in answers:
    if i == 4:
        print('D')
    elif i == 3:
        print('C')
    elif i == 2:
        print('B')
    elif i == 1:
        print('A')
    else:
        print('E')