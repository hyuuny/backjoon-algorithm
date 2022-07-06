scores = [int(input()) for _ in range(5)]
print(sum(scores) // len(scores))
print(sorted(scores)[len(scores) // 2])