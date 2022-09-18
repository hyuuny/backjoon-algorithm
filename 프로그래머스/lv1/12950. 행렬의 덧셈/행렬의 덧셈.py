def solution(arr1, arr2):
    answer = [[0] * len(i) for i in arr2]

    for i in range(len(arr1)):
        for j in range(len(arr2[i])):
            answer[i][j] = (arr1[i][j] + arr2[i][j])

    return answer


# 테스트 코드
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
