s = input()
one_cnt = 0  # 0에서 1로 바뀌는 횟수
zero_cnt = 0  # 1에서 0으로 바뀌는 횟수

if s[0] == '1':
    zero_cnt += 1
else:
    one_cnt += 1

for idx in range(len(s) - 1):
    if s[idx] != s[idx + 1]:  # 앞의 값과 다를 때,
        if s[idx + 1] == '1':
            zero_cnt += 1  # 0 -> 1이면 0 += 1,
        else:
            one_cnt += 1  # 1 -> 0이면 1 += 1

# 1과 0을 뒤집는 횟수 중, 낮은 수 출력
print(min(one_cnt, zero_cnt))