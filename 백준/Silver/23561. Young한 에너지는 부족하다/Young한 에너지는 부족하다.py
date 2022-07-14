def calculate_young_energy(energy):
    # 에너지 오름차순 정렬 후, 중간 값 가져오자.
    # n = 2면 4까지 -> 2, 3, n = 3이면, 6까지 -> 3,4,5
    sorted_energy = sorted(energy)[n:n + n]
    # 리스트에서 가장 큰 값 - 가장 작은 값
    return max(sorted_energy) - min(sorted_energy)


n = int(input())
arr = list(map(int, input().split()))
print(calculate_young_energy(arr))