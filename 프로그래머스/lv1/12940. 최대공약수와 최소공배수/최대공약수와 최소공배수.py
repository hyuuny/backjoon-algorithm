def get_max_val(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i


def get_min_val(n, m):
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            return i


def solution(n, m):
    return [get_max_val(n, m), get_min_val(n, m)]


print(solution(3, 12))
print(solution(2, 5))
