n, m = list(map(int, input().split()))

balls = [int(x + 1) for x in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    first_idx = a - 1
    second_idx = b - 1
    balls[first_idx], balls[second_idx] = balls[second_idx], balls[first_idx]

for ball in balls:
    print(ball, end=" ")