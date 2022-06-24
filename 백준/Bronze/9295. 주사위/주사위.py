n = int(input())
for i in range(n):
    dice1, dice2 = map(int, input().split())
    print('Case {}:'.format(i+1), end=" ")
    print(dice1 + dice2)