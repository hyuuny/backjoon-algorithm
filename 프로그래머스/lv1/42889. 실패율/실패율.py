def solution(N, stages):
    # 도전자 수에 맞게 빈 리스트 생성 (0번째 인덱스 사용 X)
    arr = [0] * (N + 1)

    # 각 스테이지에 머물고 있는 사용자 수로 초기화
    for i in range(len(stages)):
        if stages[i] <= N:
            arr[stages[i]] += 1

    f_rate = []  # 실패율
    user_cnt = len(stages)  # 남은 사용자 수
    for idx, count in enumerate(arr):

        # 남은 사용자가 없다면 0% !!
        if user_cnt == 0:
            f_rate.append((idx, 0))
        else:
            f_rate.append((idx, count / user_cnt))
            # 사용자 수 - 스테이지에 머무는 사용자 수
            user_cnt -= int(arr[idx])

    answer = [idx for idx, num in sorted(f_rate[1:], key=lambda x: x[1], reverse=True)]
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(3, [1, 1, 1]))
print(solution(5, [3, 3, 3, 3]))
print(solution(8, [1, 2, 3, 4, 5, 6, 7]))
