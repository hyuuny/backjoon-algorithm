input_num = int(input())
num = input_num
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1
    if new_num == input_num :break
    num = new_num
print(cnt)