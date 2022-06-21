N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

time_numbers = []
for i in range(N):
    time_numbers.append(A[i] * B[i])

print(sum(time_numbers))