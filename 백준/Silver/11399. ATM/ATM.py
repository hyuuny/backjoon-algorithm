n = int(input())
times = list(map(int, input().split()))
times.sort()  # 시간이 낮은 순 정렬

answer = 0
for i in range(len(times)):
    # 0부터 현재 인덱스 까지의 값을 차례로 더하자
    # [1,2,3,3,4] -> 1 -> 1+2 -> 1+2+3 -> 1+2+3+3 -> 1+2+3+3+4
    answer += sum(times[0:i + 1])

print(answer)