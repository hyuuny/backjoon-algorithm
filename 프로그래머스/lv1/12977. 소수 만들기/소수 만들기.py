def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(nums):
    cnt = 0
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i + 1, nums_len):
            for k in range(j + 1, nums_len):
                if is_prime_number(nums[i] + nums[j] + nums[k]):
                    cnt += 1

    return cnt


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
