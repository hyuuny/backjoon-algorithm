def iupc(arr):
    # 총 회원 수
    total_member_sum = m * k

    # 볼펜을 빌려 줄 회원 수
    pen_sum = 0

    # 볼펜을 빌려줄 회원의 수
    cnt = 0
    for i in arr:
        # 빌려줄 펜의 수보다 총 회원의 수가 더 많다면, CTP 회원의 펜을 추가로 빌려주자
        if total_member_sum > pen_sum:
            pen_sum += i
            cnt += 1

    # 펜이 부족하면 STRESS, 충분하면 회원수 출력
    print("STRESS") if total_member_sum > pen_sum else print(cnt)


n = int(input())
m, k = map(int, input().split())
iupc(sorted(list(map(int, input().split())), reverse=True))
