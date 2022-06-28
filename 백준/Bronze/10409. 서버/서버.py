n, t = map(int, input().split())
times = list(map(int, input().split()))

answer = 0
for time in times:
    if t >= time:
        t -= time
        answer += 1
    else:
        break

print(answer)