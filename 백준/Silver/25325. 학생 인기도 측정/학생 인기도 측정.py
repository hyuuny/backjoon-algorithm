def popularity(n):
    dit_names = {}
    arr = list(map(str, input().split()))
    for i in range(len(arr)):
        dit_names.setdefault(arr[i], 0)

    for _ in range(n):
        names = list(map(str, input().split()))

        for i in range(len(names)):
            dit_names[names[i]] += 1

    return dit_names


result = popularity(int(input()))
for key, val in sorted(result.items(), key=lambda x: -x[1]):
    print(key, result[key])
