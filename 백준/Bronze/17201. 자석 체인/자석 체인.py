def solve(magnet):
    for i in range(len(magnet) - 1):
        if magnet[i] == '1' and magnet[i + 1] == '1':
            return 'No'
        elif magnet[i] == '2' and magnet[i + 1] == '2':
            return 'No'

    return 'Yes'


n = int(input())
print(solve(input()))
